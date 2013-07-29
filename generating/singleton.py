# coding: utf-8

"""
Одиночка (Singleton) - паттерн, порождающий объекты.

Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.

С помощью паттерна одиночка могут быть реализованы многие паттерны (абстрактная фабрика, строитель, прототип).
"""


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        # глобальная точка доступа `Singleton.get_instance()`
        cls.get_instance = classmethod(lambda c: c._instance)
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class Singleton(object):
    __metaclass__ = SingletonMeta

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


obj1 = Singleton('MyInstance 1')
print obj1.get_name()  # MyInstance 1

obj2 = Singleton('MyInstance 2')
print obj2.get_name()  # MyInstance 1

print obj1 is obj2 is Singleton.get_instance()  # True