# coding: utf-8

"""
Команда (Command, Action, Transaction) - паттерн поведения объектов.

Инкапсулирует запрос как объект, позволяя тем самым задавать параметры клиентов
для обработки соответствующих запросов, ставить запросы в очередь или протоколировать их,
а также поддерживать отмену операций.
"""


class Light(object):
    def turn_on(self):
        print 'Включить свет'

    def turn_off(self):
        print 'Выключить свет'


class CommandBase(object):
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch(object):
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        self.on_cmd.execute()

    def off(self):
        self.off_cmd.execute()


light = Light()
switch = Switch(on_cmd=TurnOnLightCommand(light),
                off_cmd=TurnOffLightCommand(light))
switch.on()  # Включить свет
switch.off()  # Выключить свет
