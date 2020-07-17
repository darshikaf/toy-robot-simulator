#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from typing import List

from robot_simulator.agent.direction import Direction
from robot_simulator.config import Configuration
from robot_simulator.errors import InvalidParametersError, UnsupportedCommand
from robot_simulator.grid.positioning import Point


class BaseCommand(ABC):
    _COMMAND_ID = None

    @abstractmethod
    def invoke(self, target):
        pass

    @staticmethod
    def factory(config: Configuration) -> BaseCommand:
        from robot_simulator.commands.commands import PlaceCommand
        from robot_simulator.commands.commands import MoveCommand
        from robot_simulator.commands.commands import LeftCommand
        from robot_simulator.commands.commands import RightCommand
        from robot_simulator.commands.commands import ReportCommand
        from robot_simulator.commands.commands import StopCommand

        supported_commands = {
            PlaceCommand.COMMAND_ID: PlaceCommand,
            MoveCommand.COMMAND_ID: MoveCommand,
            LeftCommand.COMMAND_ID: LeftCommand,
            RightCommand.COMMAND_ID: RightCommand,
            ReportCommand.COMMAND_ID: ReportCommand,
            StopCommand.COMMAND_ID: StopCommand,
        }

        input_command_id = config.command_id
        command_ids = [
            cmd for cmd in supported_commands if cmd in input_command_id
        ]
        if not command_ids:
            raise UnsupportedCommand(input_command_id)
        command_id = command_ids[0]
        command = supported_commands[command_id]

        return command(config)
