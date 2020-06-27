DOCKER_IMAGE := darkf-build-testing:latest
TERM := docker run --rm -it -v $(shell pwd):/darkf-build-testing -w /darkf-build-testing -e PYTTHONPATH=. hub.docker.com/darshika/${DOCKER_IMAGE}
TESTENV	:= docker run --rm -v $(shell pwd):/darkf-build-testing -w /darkf-build-testing -e PYTTHONPATH=. hub.docker.com/darshika/${DOCKER_IMAGE}

clean:
	rm -rf __pycache__ alchemist/__pycache__ tests/__pycache__ .pytest_cache .coverage
	rm -rf .eggs *.egg-info dist/*

test: clean
	$(TESTENV) coverage run setup.py test --pytest-args="--junit-xml=tests/results.xml"
	$(TESTENV) coverage report

test-specific: clean
	$(TESTENV) python setup.py test --pytest-args="-k $(TEST)|-s|-v"

test-verbose: clean
	$(TESTENV) python setup.py test --pytest-args="-s"

test-missing: clean
	$(TESTENV) python setup.py test --pytest-args="--cov-report=term-missing|--cov=alchemist"

bash:
	$(TERM) bash

python:
	$(TERM) python

test-python-lint:
	$(TESTENV) /opt/conda/bin/black -l 79 --check .

test-python-types:
	$(TESTENV) /opt/conda/bin/mypy --ignore-missing-imports /alchemist

.PHONY: test bash clean python