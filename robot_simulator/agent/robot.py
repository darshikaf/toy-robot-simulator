#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robot_simulator.agent.direction import Direction
from robot_simulator.errors import MissingPlaceError, MoveOutOfBoundsError
from robot_simulator.grid.board import Board
from robot_simulator.grid.positioning import Point


class Robot:
    def __init__(self, board: Board) -> None:
        self.board = board
        self._position = None
        self._direction = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if not self.board.rect.contains(position):
            raise MoveOutOfBoundsError()

        self._position = position

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def place(self, position: Point, direction: Direction) -> None:
        self.position = position
        self.direction = direction

    def move_by(self, step: int) -> None:
        if not self._position:
            raise MissingPlaceError()

        new_position = self._position + (self._direction.vector * step)
        self.position = new_position

    def turn_by(self, step: int) -> None:
        if not self._direction:
            raise MissingPlaceError()

        new_drection = self._direction.turn_by(step)
        self.direction = new_drection

    def report(self) -> None:
        if not self._direction:
            raise MissingPlaceError()

        return f"{self._position.x},{self._position.y},{self._direction.value}"
