PYTHON ?= .venv/bin/python
PIP ?= $(PYTHON) -m pip
RUFF ?= $(PYTHON) -m ruff
PYLINT ?= $(PYTHON) -m pylint
MYPY ?= $(PYTHON) -m mypy

SOURCES = sync_rin_calendars.py

.PHONY: venv install run dry-run lint lint-fix style typecheck

venv:
	python3 -m venv .venv

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-dev.txt

run:
	$(PYTHON) sync_rin_calendars.py

dry-run:
	$(PYTHON) sync_rin_calendars.py --dry-run

lint-fix:
	$(RUFF) check --fix $(SOURCES)
	$(RUFF) format $(SOURCES)

style:
	$(RUFF) check $(SOURCES)
	$(PYLINT) $(SOURCES)

typecheck:
	$(MYPY) $(SOURCES)

lint: style typecheck
