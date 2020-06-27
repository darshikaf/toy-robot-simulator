#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InvalidParametersError(Exception):
    def __init__(self, command: str):
        super().__init__(f"Invalid parameters for {command}")


class InvalidCommandFormatError(Exception):
    def __init__(self, line: str):
        super().__init__(f"Invalid formatting of command: {line}")


class CommandNotFoundError(Exception):
    def __init__(self, command: str):
        super().__init__(f"{command} is an invalid command.")


class InvalidDirectionError(Exception):
    def __init__(self, direction: str):
        super().__init__(f"{direction} is an invalid direction.")


class MoveOutOfBoundsError(Exception):
    def __init__(self):
        super().__init__("Unable to move Robot out of bounds.")


class MissingPlaceError(Exception):
    def __init__(self):
        super().__init__("Unable to turn Robot until placed.")


class UnsupportedCommand(Exception):
    def __init__(self, cmd: str):
        super().__init__(f"{cmd} is not a supported command.")


class NoneNumericError(Exception):
    def __init__(self, coordinate: str):
        super().__init__(f"{coordinate} cannot be non-numeric.")
