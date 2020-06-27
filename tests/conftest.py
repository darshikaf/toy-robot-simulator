#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from robot_simulator.grid.board import Board
from robot_simulator.agent.robot import Robot


@pytest.fixture(scope="module")
def board():
    return Board(5, 5)


@pytest.fixture(scope="module")
def robot():
    board = Board(5, 5)
    return Robot(board)
