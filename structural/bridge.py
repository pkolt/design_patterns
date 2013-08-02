# coding: utf-8

"""
Мост (Bridge) - паттерн, структурирующий объекты.

Основная задача - отделить абстракцию от её реализации так,
чтобы то и другое можно было изменять независимо.
"""


class TVBase(object):
    """Абстрактный телевизор"""
    def tune_channel(self, channel):
        raise NotImplementedError()


class SonyTV(TVBase):
    """Телевизор Sony"""
    def tune_channel(self, channel):
        print('Sony TV: выбран %d канал' % channel)


class SharpTV(TVBase):
    """Телевизор Sharp"""
    def tune_channel(self, channel):
        print('Sharp TV: выбран %d канал' % channel)


class RemoteControlBase(object):
    """Абстрактный пульт управления"""
    def __init__(self):
        self._tv = self.get_tv()

    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Пульт управления"""
    def __init__(self):
        super(RemoteControl, self).__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return SharpTV()

    def tune_channel(self, channel):
        super(RemoteControl, self).tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


remote_control = RemoteControl()
remote_control.tune_channel(5)  # Sharp TV: выбран 5 канал
remote_control.next_channel()  # Sharp TV: выбран 6 канал
