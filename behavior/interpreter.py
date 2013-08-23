# coding: utf-8

"""
Интерпретатор (Interpreter) - паттерн поведения классов.

Для заданного языка определяет представление его грамматики,
а также интерпретатор предложений этого языка.
"""


class RomanNumeralInterpreter(object):
    """Интерпретатор римских цифр"""
    def __init__(self):
        self.grammar = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def interpret(self, text):
        numbers = map(self.grammar.get, text)  # строки в значения
        if None in numbers:
            raise ValueError('Ошибочное значение: %s' % text)
        result = 0  # накапливаем результат
        temp = None  # запоминаем последнее значение
        while numbers:
            num = numbers.pop(0)
            if temp is None or temp >= num:
                result += num
            else:
                result += (num - temp * 2)
            temp = num
        return result


interp = RomanNumeralInterpreter()
print interp.interpret('MMMCMXCIX') == 3999  # True
print interp.interpret('MCMLXXXVIII') == 1988  # True
