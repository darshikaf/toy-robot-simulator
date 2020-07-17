DOCKER_IMAGE := darkf-build-testing:latest
TERM := docker run --rm -it -v $(shell pwd):/robot_simulator -w /robot_simulator -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}
TESTENV	:= docker run --rm -v $(shell pwd):/robot_simulator -w /robot_simulator -e PYTTHONPATH=. darshika/${DOCKER_IMAGE}

clean:
	rm -rf __pycache__ robot_simulator/__pycache__ tests/__pycache__ .pytest_cache .coverage
	rm -rf __pycache__ robot_simulator/grid/__pycache__ robot_simulator/agent/__pycache__ robot_simulator/commands/__pycache__
	rm -rf .mypy_cache/
	rm -rf .eggs *.egg-info dist/*

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

test-python-lint:
	$(TESTENV) black -l 79 --check .

test-python-types:
	$(TESTENV) mypy --ignore-missing-imports robot_simulator

.PHONY: test bash clean python