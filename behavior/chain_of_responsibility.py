# coding: utf-8

"""
Цепочка обязанностей (Chain of Responsibility) - паттерн поведения объектов.

Позволяет избежать привязки отправителя запроса к его получателю,
давая шанс обработать запрос нескольким объектам. Связывает объекты-получатели в цепочку
и передает запрос вдоль этой цепочки, пока его не обработают.
"""


class HttpHandler(object):
    """Абстрактный класс обработчика"""
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(HttpHandler):
    """Обработчик для кода 404"""
    def handle(self, code):
        if code == 404:
            return 'Страница не найдена'


class Http500Handler(HttpHandler):
    """Обработчик для кода 500"""
    def handle(self, code):
        if code == 500:
            return 'Ошибка сервера'


class Client(object):
    def __init__(self):
        self._handlers = []

    def add_handler(self, h):
        self._handlers.append(h)

    def response(self, code):
        for h in self._handlers:
            msg = h.handle(code)
            if msg:
                print 'Ответ: %s' % msg
                break
        else:
            print 'Код не обработан'


client = Client()
client.add_handler(Http404Handler())
client.add_handler(Http500Handler())
client.response(400)  # Код не обработан
client.response(404)  # Ответ: Страница не найдена
client.response(500)  # Ответ: Ошибка сервера
