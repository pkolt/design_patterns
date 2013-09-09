# coding: utf-8

"""
Состояние (State) - паттерн поведения объектов.

Позволяет объекту варьировать свое поведение в зависимости от внутреннего состояния.
Извне создается впечатление, что изменился класс объекта.
"""


class LampStateBase(object):
    """Состояние лампы"""
    def get_color(self):
        raise NotImplementedError()


class GreenLampState(LampStateBase):
    def get_color(self):
        return 'Green'


class RedLampState(LampStateBase):
    def get_color(self):
        return 'Red'


class BlueLampState(LampStateBase):
    def get_color(self):
        return 'Blue'


class Lamp(object):
    def __init__(self):
        self._current_state = None
        self._states = self.get_states()

    def get_states(self):
        return [GreenLampState(), RedLampState(), BlueLampState()]

    def next_state(self):
        if self._current_state is None:
            self._current_state = self._states[0]
        else:
            index = self._states.index(self._current_state)
            if index < len(self._states) - 1:
                index += 1
            else:
                index = 0
            self._current_state = self._states[index]
        return self._current_state

    def light(self):
        state = self.next_state()
        print state.get_color()


lamp = Lamp()
[lamp.light() for i in range(3)]
# Green
# Red
# Blue
[lamp.light() for i in range(3)]
# Green
# Red
# Blue
