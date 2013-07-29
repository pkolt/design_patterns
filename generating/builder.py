# coding: utf-8

"""
Строитель (Builder) - паттерн, порождающий объекты.

Отделяет конструирование сложного объекта от его представления,
так что в результате одного и того же процесса конструирования могут получаться разные представления.

От абстрактной фабрики отличается тем, что делает акцент на пошаговом конструировании объекта.
Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика возвращает объект немедленно.

Строитель часто используется для создания паттерна компоновщик.
"""


class Builder(object):
    def build_body(self):
        raise NotImplementedError()

    def build_lamp(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def create_flashlight(self):
        raise NotImplementedError()


class Flashlight(object):
    """Карманный фонарик"""
    def __init__(self, body, lamp, battery):
        self._shine = False  # излучать свет
        self._body = body
        self._lamp = lamp
        self._battery = battery

    def on(self):
        self._shine = True

    def off(self):
        self._shine = False

    def __str__(self):
        shine = 'on' if self._shine else 'off'
        return 'Flashlight [%s]' % shine


class Lamp(object):
    """Лампочка"""


class Body(object):
    """Корпус"""


class Battery(object):
    """Батарея"""


class FlashlightBuilder(Builder):
    def build_body(self):
        return Body()

    def build_battery(self):
        return Battery()

    def build_lamp(self):
        return Lamp()

    def create_flashlight(self):
        body = self.build_body()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return Flashlight(body, lamp, battery)


builder = FlashlightBuilder()
flashlight = builder.create_flashlight()
flashlight.on()
print flashlight  # Flashlight [on]