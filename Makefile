SHELL := /bin/bash
.SILENT:
.DEFAULT_GOAL := help

SYS_PY3=$(shell which python3)
VENV_DIR=./venv
VENV_PY3=$(VENV_DIR)/bin/python
VENV_PIP3=$(VENV_DIR)/bin/pip

LAST_TASK_NUM=$(shell find tasks -name 'task*.py' | sort -V | tail -1 | sed -r 's/tasks\/task([0-9]*).*/\1/' | sed -E 's/^0+//' )
NEW_TASK_NAME=$(shell printf 'task%04d' $$(( ${LAST_TASK_NUM} + 1)) )
NEW_TEST_NAME=$(shell printf 'test_task%04d' $$(( ${LAST_TASK_NUM} + 1)) )

.PHONY: venv
## Create virtual environment
venv:
	$(SYS_PY3) -m venv $(VENV_DIR)

.PHONY: install-deps
## Update pip and install all requirements from requirements.txt
install-deps: requirements.txt
	$(VENV_PIP3) install --upgrade pip setuptools wheel && $(VENV_PIP3) install -r requirements.txt

.PHONY: pytest
## Run pytest for testing
pytest: clean-pyc
	$(VENV_PY3) -m py.test

.PHONY: isort
## Run isort linter
isort:
	$(VENV_PY3) -m isort tasks/
	$(VENV_PY3) -m isort tests/

.PHONY: black
## Run black linter
black:
	$(VENV_PY3) -m black tasks/
	$(VENV_PY3) -m black tests/

.PHONY: flake8
## Run flake8 linter
flake8:
	$(VENV_PY3) -m flake8 tasks/
	$(VENV_PY3) -m flake8 tests/


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
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) == Darwin && echo '--no-init --raw-control-chars')

