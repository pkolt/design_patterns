# coding: utf-8

"""
Декоратор (Decorator, Wrapper) - паттерн, структурирующий объекты.

Динамически добавляет объекту новые обязанности.
Является гибкой альтернативой порождению подклассов с целью расширения функциональности.
"""


class Man(object):
    """Человек"""
    def __init__(self, name):
        self._name = name

    def say(self):
        print 'Привет! Меня зовут %s!' % self._name


class Jetpack(object):
    """Реактивный ранец"""
    def __init__(self, man):
        self._man = man

    def __getattr__(self, item):
        return getattr(self._man, item)

    def fly(self):
        # расширяем функциональность объекта добавляя возможность летать
        print '%s летит на реактивном ранце!' % self._man._name


man = Man('Виктор')

man_jetpack = Jetpack(man)
man_jetpack.say()  # Привет! Меня зовут Виктор!
man_jetpack.fly()  # Виктор летит на реактивном ранце!
