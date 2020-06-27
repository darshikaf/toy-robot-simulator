#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from robot_simulator.grid.board import Board
from robot_simulator.errors import MoveOutOfBoundsError, MissingPlaceError
from robot_simulator.agent.direction import Direction
from robot_simulator.grid.positioning import Point
from robot_simulator.agent.robot import Robot


def test_place(board, robot):
    robot.place(Point(0, 1), Direction("NORTH"))

    assert robot.position == Point(0, 1)
    assert robot.direction == Direction("NORTH")


def test_place_out_of_lower_bounds(board, robot):
    with pytest.raises(MoveOutOfBoundsError):
        robot.place(Point(4, 5), Direction("NORTH"))


def test_place_out_of_upper_bounds(board, robot):
    with pytest.raises(MoveOutOfBoundsError):
        robot.place(Point(-1, 3), Direction("EAST"))


def test_move(board, robot):
    robot.place(Point(0, 1), Direction("NORTH"))
    robot.move_by(1)

    assert robot.position == Point(0, 2)
    assert robot.direction == Direction("NORTH")


def test_move_without_place():
    board = Board(5, 5)
    robot = Robot(board)

    with pytest.raises(
        MissingPlaceError, match="Unable to turn Robot until placed."
    ):
        robot.move_by(1)


def test_move_out_of_lower_bounds(board, robot):
    with pytest.raises(MoveOutOfBoundsError):
        robot.place(Point(0, 4), Direction("WEST"))
        robot.move_by(1)


def test_move_out_of_upper_bounds(board, robot):
    with pytest.raises(MoveOutOfBoundsError):
        robot.place(Point(4, 0), Direction("SOUTH"))
        robot.move_by(1)


def test_left(board, robot):
    robot.place(Point(2, 4), Direction("NORTH"))
    robot.turn_by(-1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("WEST")

    robot.turn_by(-1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("SOUTH")

    robot.turn_by(-1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("EAST")

    robot.turn_by(-1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("NORTH")


def test_left_without_place():
    board = Board(5, 5)
    robot = Robot(board)

    with pytest.raises(
        MissingPlaceError, match="Unable to turn Robot until placed."
    ):
        robot.turn_by(-1)


def test_right(board, robot):
    robot.place(Point(2, 4), Direction("NORTH"))
    robot.turn_by(1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("EAST")

    robot.turn_by(1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("SOUTH")

    robot.turn_by(1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("WEST")

    robot.turn_by(1)

    assert robot.position == Point(2, 4)
    assert robot.direction == Direction("NORTH")


def test_right_without_place():
    board = Board(5, 5)
    robot = Robot(board)

    with pytest.raises(
        MissingPlaceError, match="Unable to turn Robot until placed."
    ):
        robot.turn_by(1)


def test_report(board, robot):
    robot.place(Point(2, 4), Direction("NORTH"))

    assert robot.report() == "2,4,NORTH"


def test_report_without_place():
    board = Board(5, 5)
    robot = Robot(board)

    with pytest.raises(
        MissingPlaceError, match="Unable to turn Robot until placed."
    ):
        robot.report()
