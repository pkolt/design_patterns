# coding: utf-8

"""
Фасад (Facade) - паттерн, структурирующий объекты.

Предоставляет унифицированный интерфейс вместо набора интерфейсов некоторой подсистемы.
Фасад определяет интерфейс более высокого уровня, который упрощает использование подсистемы.
"""


class Paper(object):
    """Бумага"""
    def __init__(self, count):
        self._count = count

    def get_count(self):
        return self._count

    def draw(self, text):
        if self._count > 0:
            self._count -= 1
            print text


class Printer(object):
    """Принтер"""
    def error(self, msg):
        print 'Ошибка: %s' % msg

    def print_(self, paper, text):
        if paper.get_count() > 0:
            paper.draw(text)
        else:
            self.error('Бумага закончилась')


class Facade(object):
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def write(self, text):
        self._printer.print_(self._paper, text)


f = Facade()
f.write('Hello world!')  # Hello world!
f.write('Hello world!')  # Ошибка: Бумага закончилась
