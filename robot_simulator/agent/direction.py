#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from robot_simulator.errors import InvalidDirectionError
from robot_simulator.grid.positioning import Vector


class Direction:
    VALUES = ["NORTH", "EAST", "SOUTH", "WEST"]
    NORTH, EAST, SOUTH, WEST = VALUES
    VECTORS = {
        NORTH: Vector(0, 1),
        EAST: Vector(1, 0),
        SOUTH: Vector(0, -1),
        WEST: Vector(-1, 0),
    }

    def __init__(self, value: str) -> None:
        if value not in self.VALUES:
            raise InvalidDirectionError(value)
        self.value = value
        self.vector = self.VECTORS[value]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Direction):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Direction):
            return not (self == other)
        return NotImplemented

    def turn_by(self, step: int) -> Direction:
        index = self.VALUES.index(self.value)
        new_index = (index + step) % len(self.VALUES)
        new_value = self.VALUES[new_index]
        return self.__class__(new_value)
