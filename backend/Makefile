.PHONY: install run test lint format migrate seed

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m flask --app app run --debug

test:
	$(PYTHON) -m pytest -v

lint:
	$(VENV)/bin/ruff check .

format:
	$(VENV)/bin/ruff format .

migrate:
	$(PYTHON) -m flask --app app db upgrade

seed:
	$(PYTHON) seed.py