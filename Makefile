DOCKER_IMAGE := build-python:latest
TERM := docker run --rm -it -v $(shell pwd):/robot_simulator -w /robot_simulator -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}
TESTENV	:= docker run --rm -v $(shell pwd):/robot_simulator -w /robot_simulator -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}

clean:
	$(TESTENV) rm -rf __pycache__ robot_simulator/__pycache__ tests/__pycache__ .pytest_cache .coverage
	$(TESTENV) rm -rf __pycache__ robot_simulator/grid/__pycache__ robot_simulator/agent/__pycache__ robot_simulator/commands/__pycache__
	$(TESTENV) rm -rf .mypy_cache/
	$(TESTENV) rm -rf .eggs *.egg-info dist/*

test: clean
	$(TESTENV) coverage run setup.py test --pytest-args="--junit-xml=tests/results.xml"
	$(TESTENV) coverage report

test-specific: clean
	$(TESTENV) python setup.py test --pytest-args="-k $(TEST)|-s|-v"

test-verbose: clean
	$(TESTENV) python setup.py test --pytest-args="-s"

test-missing: clean
	$(TESTENV) python setup.py test --pytest-args="--cov-report=term-missing|--cov=robot_simulator"

bash:
	$(TERM) bash

python:
	$(TERM) python

release:
	$(TERM) python setup.py sdist bdist_wheel; twine upload --repository testpypi dist/*

test-python-lint:
	$(TESTENV) black -l 79 --check .

test-python-types:
	$(TESTENV) mypy --ignore-missing-imports robot_simulator

.PHONY: test bash clean python