# coding: utf-8

"""
Приспособленец (Flyweight) - паттерн, структурирующий объекты.

Использует разделение для эффективной поддержки множества мелких объектов.
"""

import weakref


class Color(object):
    """Приспособленец"""
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ColorFactory(object):
    """Фабрика приспособленцев"""
    _colors = weakref.WeakValueDictionary()

    @classmethod
    def get_color(cls, name):
        value = cls._colors.get(name)
        if value is None:
            value = Color(name)
            cls._colors[name] = value
        return value


class Placemark(object):
    """Метка на карте"""
    def __init__(self, latitude, longitude, color_name):
        # координаты - внутреннее состояние (т.к. они уникальны для каждой метки)
        self._latitude = latitude
        self._longitude = longitude
        # цвет - внешнее состояние которое может быть общим у разных меток
        self._color = ColorFactory.get_color(color_name)

    def __str__(self):
        args = (self._color, self._latitude, self._longitude)
        return 'Цвет: %s; Координаты: (%0.4f, %0.4f)' % args


plmrk0 = Placemark(-74.007121, 40.714551, 'green')  # Нью-Йорк
plmrk1 = Placemark(37.617761, 55.755773, 'green')  # Москва

print plmrk0  # Цвет: green; Координаты: (-74.0071, 40.7146)
print plmrk1  # Цвет: green; Координаты: (37.6178, 55.7558)
print plmrk0._color is plmrk1._color  # True
