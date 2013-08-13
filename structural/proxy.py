# coding: utf-8

"""
Заместитель (Proxy, Surrogate) - паттерн, структурирующий объекты.

Является суррогатом другого объекта и контролирует доступ к нему.
"""


from functools import partial


class ImageBase(object):
    """Абстрактное изображение"""
    @classmethod
    def create(cls, width, height):
        """Создает изображение"""
        return cls(width, height)

    def draw(self, x, y, color):
        """Рисует точку заданным цветом"""
        raise NotImplementedError()

    def fill(self, color):
        """Заливка цветом"""
        raise NotImplementedError()

    def save(self, filename):
        """Сохраняет изображение в файл"""
        raise NotImplementedError()


class Image(ImageBase):
    """Изображение"""
    def __init__(self, width, height):
        self._width = int(width)
        self._height = int(height)

    def draw(self, x, y, color):
        print 'Рисуем точку; координаты: (%d, %d); цвет: %s' % (x, y, color)

    def fill(self, color):
        print 'Заливка цветом %s' % color

    def save(self, filename):
        print 'Сохраняем изображение в файл %s' % filename


class ImageProxy(ImageBase):
    """
    Заместитель изображения.
    Откладывает выполнение операций над изображением до момента его сохранения.
    """
    def __init__(self, *args, **kwargs):
        self._image = Image(*args, **kwargs)
        self.operations = []

    def draw(self, *args):
        func = partial(self._image.draw, *args)
        self.operations.append(func)

    def fill(self, *args):
        func = partial(self._image.fill, *args)
        self.operations.append(func)

    def save(self, filename):
        # выполняем все операции над изображением
        map(lambda f: f(), self.operations)
        # сохраняем изображение
        self._image.save(filename)


img = ImageProxy(200, 200)
img.fill('gray')
img.draw(0, 0, 'green')
img.draw(0, 1, 'green')
img.draw(1, 0, 'green')
img.draw(1, 1, 'green')
img.save('image.png')

# Заливка цветом gray
# Рисуем точку; координаты: (0, 0); цвет: green
# Рисуем точку; координаты: (0, 1); цвет: green
# Рисуем точку; координаты: (1, 0); цвет: green
# Рисуем точку; координаты: (1, 1); цвет: green
# Сохраняем изображение в файл image.png
