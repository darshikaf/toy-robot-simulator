#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

from robot_simulator import __version__

requirements = ["click==7.1.2", "typing>=3.6.2"]
test_requirements = ["coverage", "pytest", "pytest-cov"]


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args.split("|"))
        sys.exit(errno)


setup(
    name="robot-simulator",
    version=__version__,
    description="CLI tool that simulates movements of an agent (robot) on a specified area.",
    long_description=open("README.md").read(),
    author="Jane Doe",
    author_email="Jane.Doe@company.com.au",
    keywords="cli",
    packages=find_packages(include=["robot_simulator"]),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["robotsimulator = robot_simulator.cli:main"]
    },
    test_suite="tests",
    tests_require=test_requirements,
    cmdclass={"test": PyTest},
)
