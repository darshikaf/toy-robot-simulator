# Robot-Simulator
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Robot-Simulator](#robot-simulator)
  - [Overview](#overview)
  - [Usage](#usage)
    - [Commands](#commands)
    - [Examples](#examples)
  - [Development](#development)

<!-- /code_chunk_output -->


## Overview

Robot-Simulator is a CLI tool that simulates movements of an agent (robot) on a specified area.

This simulator currently supports interactive inputs from terminal and inputs from a file.

**`$robotsimulator start`** will start an interative session where commands for movement can be given sequentially.

**`$robotsimulator start --file-path /path/to/file`** is used to provide a path to a file that contains the commands for movememt.

## Usage

Install robot package as:
```sh
$conda create -n <venv_name> python=3.8
$conda activate <venv_name>

$cd REA_toy_robot_v5/toy_robot
$pip install .
```

To verify successful installation:

`$robotsimulator --version`

For help options:
`$robotsimulator --help`

### Commands

* Area allowed for movement is of the size 5x5.

* Supported Commands:

- `PLACE <x-coordinate> <y-coordinate> <direction>`
- `MOVE`
- `LEFT`
- `RIGHT` 
- `REPORT`
- `STOP`

* Commands are not case sensitive.
* Commands should always start with a `PLACE` command to define initial position of the agent.
* `MOVE` will move the agent by unit in the direction defined in `PLACE`.
* `LEFT` and `RIGHT` will update the direction relative to current direction defined in `PLACE`.
* If a movement is out of bounds of the area allowed for movement, the movement will be ignored and user will be prompted for another command.
* `REPORT` will display the current position of the agent in the format of `<x-coordinate> <y-coordinate> <direction>`.
* To exit a session use command `STOP` or `CTRL` `+` `D`.

### Examples

**Example a**
```sh
    $robotsimulator start
    PLACE 0,0,NORTH
    MOVE
    REPORT
```
Expected output:
```sh
    Current Position: 0,1,NORTH
```
**Example b**
```sh
    $robotsimulator start
    place 0,0,north
    left
    REPORT
```
Expected output:
```sh
    Current Position: 0,0,WEST
```
**Example c**
```sh
    $robotsimulator start
    PLACE 1,2,EAST
    MOVE
    MOVE
    LEFT
    MOVE
    REPORT
```
Expected output
```sh
    Current Position: 3,3,NORTH
```
**Example d**
```sh
    $robotsimulator start --file-path /path/to/file.txt
```
Content of the file
```
    PLACE 3,3,NORTH
    REPORT
```
Expected output
```sh
    Current Position: 3,3,NORTH
```
**Example d**
```sh
    $robotsimulator start
    PLACE 3,3,NORTH
    REPORT
```
Expected output
```sh
    Current Position: 3,3,NORTH
    Exiting the session.
```


## Development

* Dependencies

- access to [Dockerhub](https://hub.docker.com/).
- Conda environment with Python 3.8.

* Installation
```sh
cd REA_toy_robot_v5/toy_robot

pip install -e .
```

* Testing
```sh
$make test
```

* Linting
```sh
$make test-python-lint
```

* Type checking
```sh
$make test-python-type
```

Credit to https://github.com/jessehon/robot-simulator/tree/master for the framework idea.

