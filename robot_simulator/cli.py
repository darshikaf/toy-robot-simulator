#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import Any, List, TextIO

import click

from robot_simulator.commands.base import BaseCommand
from robot_simulator.config import Configuration
from robot_simulator.simulation import Simulation
from robot_simulator import __version__


@click.group()
@click.version_option(__version__)
def cli() -> None:
    """
  Simulates movements of an agent on a specified area with controlled movements.
  This simulator currently supports interactive inputs from terminal and inputs from a file.

  Please refer to https://github.com/janedoe/toy-robot/blob/master/README.md for installation and usage instructions.
    
  """
    pass


@cli.command(help="Starts simulation.")
@click.option(
    "--file-path", help="Path to commands file.", type=click.File("r")
)
def start(file_path: TextIO) -> None:
    if file_path:
        with file_path as f:
            data = f.read()
        lines = data.split("\n")
        execute(lines)

    execute(sys.stdin)


def execute(line: List[str]) -> None:
    simulation = Simulation()

    for cmd in line:
        config = Configuration(cmd)
        command = BaseCommand.factory(config)
        simulation.run(command)


def main() -> None:
    cli()
