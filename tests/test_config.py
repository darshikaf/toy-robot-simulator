#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from robot_simulator.config import Configuration
from robot_simulator.errors import (
    CommandNotFoundError,
    InvalidCommandFormatError,
    NoneNumericError,
)


def _placement_command(x, y, f):
    return f"PLACE {x},{y},{f}"


def _invalid_placement_command(x, y, f):
    return f"PLACE {x},{y},{f}"


def _move_command():
    return "MOVE"


def _turn_left_command():
    return "LEFT"


def _turn_right_command():
    return "RIGHT"


def _report_command():
    return "REPORT"


def test_placement():
    place = _placement_command("1", "2", "NORTH")
    config = Configuration(place)

    assert config.command_id == "PLACE"
    assert config.x == "1"
    assert config.y == "2"
    assert config.direction == "NORTH"


def test_movement():
    move = _move_command()
    config = Configuration(move)

    assert config.command_id == "MOVE"
    assert config.x == None
    assert config.y == None
    assert config.direction == None


def test_left_turn():
    right = _turn_left_command()
    config = Configuration(right)

    assert config.command_id == "LEFT"
    assert config.x == None
    assert config.y == None
    assert config.direction == None


def test_right_turn():
    right = _turn_right_command()
    config = Configuration(right)

    assert config.command_id == "RIGHT"
    assert config.x == None
    assert config.y == None
    assert config.direction == None


def test_report():
    right = _report_command()
    config = Configuration(right)

    assert config.command_id == "REPORT"
    assert config.x == None
    assert config.y == None
    assert config.direction == None


def test_non_numeric_coordinate_in_placement():
    with pytest.raises((InvalidCommandFormatError, NoneNumericError)):
        place = _placement_command("A", "0", "NORTH")
        config = Configuration(place)


def test_additional_whitespaces_in_placement():
    with pytest.raises(InvalidCommandFormatError):
        place = _placement_command("0 ", "0", "NORTH")
        config = Configuration(place)
