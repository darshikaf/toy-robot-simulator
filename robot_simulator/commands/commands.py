#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from robot_simulator.agent.direction import Direction
from robot_simulator.commands.base import BaseCommand
from robot_simulator.config import Configuration
from robot_simulator.errors import InvalidParametersError
from robot_simulator.grid.positioning import Point


class PlaceCommand(BaseCommand):
    COMMAND_ID = "PLACE"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        self._position = Point(int(self.x), int(self.y))
        self._direction = Direction(self.direction)
        target.place(self._position, self._direction)


class MoveCommand(BaseCommand):
    COMMAND_ID = "MOVE"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        target.move_by(1)


class LeftCommand(BaseCommand):
    COMMAND_ID = "LEFT"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        target.turn_by(-1)


class RightCommand(BaseCommand):
    COMMAND_ID = "RIGHT"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        target.turn_by(1)


class ReportCommand(BaseCommand):
    COMMAND_ID = "REPORT"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        print(f"Current Position: {target.report()}")


class StopCommand(BaseCommand):
    COMMAND_ID = "STOP"

    def __init__(self, config: Configuration) -> None:
        self.__dict__ = config.__dict__.copy()

    def invoke(self, target):
        print("Exiting the session...")
        sys.exit()
