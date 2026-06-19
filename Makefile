SHELL := /bin/bash
.SILENT:
.DEFAULT_GOAL := help

UV=uv
SRC=tasks/ tests/

LAST_TASK_NUM=$(shell find tasks -name 'task*.py' | sort -V | tail -1 | sed -r 's/tasks\/task([0-9]*).*/\1/' | sed -E 's/^0+//' )
NEW_TASK_NAME=$(shell printf 'task%04d' $$(( ${LAST_TASK_NUM} + 1)) )
NEW_TEST_NAME=$(shell printf 'test_task%04d' $$(( ${LAST_TASK_NUM} + 1)) )

.PHONY: venv
## Create virtual environment with uv
venv:
	$(UV) venv

.PHONY: install-deps
## Sync all dependencies from pyproject.toml/uv.lock
install-deps: pyproject.toml
	$(UV) sync

.PHONY: lock
## Regenerate uv.lock from pyproject.toml
lock:
	$(UV) lock

.PHONY: pytest
## Run pytest for testing
pytest: clean-pyc
	$(UV) run pytest

.PHONY: isort
## Run isort linter
isort:
	$(UV) run isort $(SRC)

.PHONY: black
## Run black linter
black:
	$(UV) run black $(SRC)

.PHONY: flake8
## Run flake8 linter
flake8:
	$(UV) run flake8 $(SRC)

.PHONY: test
## Run all linters and tests
test: isort black flake8 pytest clean

.PHONY: newtask
## Add new task with test file
newtask:
	touch tasks/${NEW_TASK_NAME}.py
	touch tests/${NEW_TEST_NAME}.py

.PHONY: lint
## Run only linters
lint: isort black flake8 clean

.PHONY: clean-cache
## Remove directory with cached files
clean-cache:
	find ./tasks -type d -name '__pycache__' -exec rm -rf {} +
	find ./tests -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +

.PHONY: clean-pyc
## Clean binary compiled files
clean-pyc:
	find ./tasks -name '*.pyc' -exec rm -rf {} + ;
	find ./tasks -name '*.pyo' -exec rm -rf {} + ;
	find ./tests -name '*.pyc' -exec rm -rf {} + ;
	find ./tests -name '*.pyo' -exec rm -rf {} + ;

.PHONY: clean
## Clean all artifacts
clean: clean-cache clean-pyc

.PHONY: help
## Show this help message
help:
	@printf "\033[1mAvailable rules:\033[0m\n\n"
	@awk 'BEGIN { FS = ":" } \
		/^## / { doc = substr($$0, 4); next } \
		/^[a-zA-Z0-9_-]+:/ { if (doc) printf "  \033[36m%-18s\033[0m %s\n", $$1, doc; doc = "" } \
		{ doc = "" }' $(MAKEFILE_LIST) \
	| LC_ALL='C' sort --ignore-case

