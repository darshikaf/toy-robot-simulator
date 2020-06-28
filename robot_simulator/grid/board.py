#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robot_simulator.grid.positioning import Point, Rect


class Board:
    def __init__(self, size_x, size_y):
        bottom_left = Point(0, 0)
        top_right = Point(size_x - 1, size_y - 1)
        self.rect = Rect(bottom_left, top_right)
