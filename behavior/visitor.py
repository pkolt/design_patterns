# coding: utf-8

"""
Постетитель (Visitor) - паттерн поведения объектов.

Описывает операцию, выполняемую с каждым объектом из некоторой структуры.
Паттерн посетитель позволяет определить новую операцию, не изменяя классы этих объектов.
"""


class FruitVisitor(object):
    """Посетитель"""
    def draw(self, fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)
        draw(fruit)

    def draw_apple(self, fruit):
        print 'Яблоко'

    def draw_pear(self, fruit):
        print 'Груша'

    def draw_unknown(self, fruit):
        print 'Фрукт'


class Fruit(object):
    """Фрукты"""
    def draw(self, visitor):
        visitor.draw(self)


class Apple(Fruit):
    """Яблоко"""


class Pear(Fruit):
    """Груша"""


class Banana(Fruit):
    """Банан"""


visitor = FruitVisitor()

apple = Apple()
apple.draw(visitor)
# Яблоко

pear = Pear()
pear.draw(visitor)
# Груша

banana = Banana()
banana.draw(visitor)
# Фрукт
