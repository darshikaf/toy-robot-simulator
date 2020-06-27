#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from robot_simulator.commands.base import BaseCommand
from robot_simulator.config import Configuration
from robot_simulator.agent.direction import Direction
from robot_simulator.errors import InvalidParametersError
from robot_simulator.grid.positioning import Point, Vector


def _placement_config():
    return Configuration("PLACE 1,2,NORTH")


def _movement_config():
    return Configuration("MOVE")


def _left_turn_config():
    return Configuration("LEFT")


def _right_turn_config():
    return Configuration("RIGHT")


def _report_config():
    return Configuration("REPORT")


def test_place(board, robot):
    config = _placement_config()
    command = BaseCommand.factory(config)

    assert command.COMMAND_ID == "PLACE"

    command.invoke(robot)

    assert robot.position == Point(1, 2)
    assert robot.direction == Direction("NORTH")


def test_move(board, robot):
    config = _movement_config()
    command = BaseCommand.factory(config)

    assert command.COMMAND_ID == "MOVE"

    command.invoke(robot)

    assert robot.position == Point(1, 3)
    assert robot.direction == Direction("NORTH")


def test_turn_left(board, robot):
    config = _left_turn_config()
    command = BaseCommand.factory(config)

    assert command.COMMAND_ID == "LEFT"

    command.invoke(robot)

    assert robot.position == Point(1, 3)
    assert robot.direction == Direction("WEST")


def test_turn_right(board, robot):
    config = _right_turn_config()
    command = BaseCommand.factory(config)

    assert command.COMMAND_ID == "RIGHT"

    command.invoke(robot)

    assert robot.position == Point(1, 3)
    assert robot.direction == Direction("NORTH")


def test_report(board, robot):
    config = _report_config()
    command = BaseCommand.factory(config)

    assert command.COMMAND_ID == "REPORT"
