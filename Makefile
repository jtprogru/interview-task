SHELL := /bin/bash

.PHONY: default test-full isort clean-pyc clean-full


default: test-full

venv:
	python3 -m venv venv && source venv/bin/activate

install-deps: requirements.txt
	./venv/bin/pip install -r requirements.txt

pytest: clean-pyc
	./venv/bin/python -m py.test

isort:
	./venv/bin/python -m isort tasks/
	./venv/bin/python -m isort tests/

black:
	./venv/bin/python -m black tasks/
	./venv/bin/python -m black tests/

flake8:
	./venv/bin/python -m flake8 tasks/
	./venv/bin/python -m flake8 tests/

test-full: isort black flake8 pytest

clean-cache:
	find ./tasks -type d -name '__pycache__' -exec rm -rf {} +
	find ./tests -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

clean-pyc:
	find ./tasks -name '*.pyc' -exec rm -rf {} + ;
	find ./tasks -name '*.pyo' -exec rm -rf {} + ;
	find ./tests -name '*.pyc' -exec rm -rf {} + ;
	find ./tests -name '*.pyo' -exec rm -rf {} + ;

clean-full: clean-cache clean-pyc
