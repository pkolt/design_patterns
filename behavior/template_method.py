# coding: utf-8

"""
Шаблонный метод (Template method) - паттерн поведения классов.

Шаблонный метод определяет основу алгоритма и позволяет подклассам переопределить некоторые шаги алгоритма,
не изменяя его структуру в целом.
"""


class ExampleBase(object):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        raise NotImplementedError()

    def step_two(self):
        raise NotImplementedError()

    def step_three(self):
        raise NotImplementedError()


class Example(ExampleBase):
    def step_one(self):
        print 'Первый шаг алгоритма'

    def step_two(self):
        print 'Второй шаг алгоритма'

    def step_three(self):
        print 'Третий шаг алгоритма'


example = Example()
example.template_method()

# Первый шаг алгоритма
# Второй шаг алгоритма
# Третий шаг алгоритма
