#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robot_simulator.grid.board import Board
from robot_simulator.commands.base import BaseCommand
from robot_simulator.errors import MoveOutOfBoundsError, MissingPlaceError
from robot_simulator.agent.robot import Robot


class Simulation:
    def __init__(self) -> None:
        self.board = Board(5, 5)
        self.robot = Robot(self.board)

    def run(self, command: BaseCommand) -> None:
        try:
            command.invoke(target=self.robot)
        except MoveOutOfBoundsError as e:
            print(f"Skip {command.COMMAND_ID}: {e}")
        except MissingPlaceError as e:
            print(f"Skip {command.COMMAND_ID}: {e}")
