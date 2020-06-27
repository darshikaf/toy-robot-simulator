#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robot_simulator.errors import InvalidCommandFormatError, NoneNumericError


class Configuration:
    def __init__(self, line: str) -> None:
        self.x = self._parse_position(line, flag="X")
        self.y = self._parse_position(line, flag="Y")
        self.direction = self._parse_position(line, flag="F")
        self.command_id = self._parse_command(line)

    def _parse_command(self, line: str) -> str:
        if line.split()[
            0
        ]:  # TODO: split by regex to handle whitespaces, handle casesensitive
            return line.split()[0]
        return None

    def _parse_position(self, line: str, flag: str) -> str:
        if line.split()[0] == "PLACE":
            try:
                if flag == "X":
                    x = line.split()[1].split(",")[0]
                    if not x.isnumeric():
                        raise NoneNumericError(flag)
                    return x
                if flag == "Y":
                    y = line.split()[1].split(",")[1]
                    if not y.isnumeric():
                        raise NoneNumericError(flag)
                    return y
                if flag == "F":
                    return line.split()[1].split(",")[2]
            except:
                raise InvalidCommandFormatError(line)
        return None
