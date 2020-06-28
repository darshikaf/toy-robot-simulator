#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

import math


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return (self.x == other.x) and (self.y == other.y)
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Point):
            return not (self == other)
        return NotImplemented

    def __add__(self, other: Point) -> Point:
        x = self.x + other.x
        y = self.y + other.y
        return self.__class__(x, y)


class Vector(Point):
    def __mul__(self, scale: int) -> Vector:
        x = self.x * scale
        y = self.y * scale
        return self.__class__(x, y)


class Rect:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.top = max(point1.y, point2.y)
        self.right = max(point1.x, point2.x)
        self.bottom = min(point1.y, point2.y)
        self.left = min(point1.x, point2.x)

    def contains(self, point: Point) -> bool:
        contains_x = (self.left <= point.x) and (point.x <= self.right)
        contains_y = (self.bottom <= point.y) and (point.y <= self.top)
        return contains_x and contains_y
