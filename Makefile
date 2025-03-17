PYTHON = python3
PIP = $(PYTHON) -m pip
PYTEST = $(PYTHON) -m pytest
FLAKE8 = $(PYTHON) -m flake8
MYPY = $(PYTHON) -m mypy
BLACK = $(PYTHON) -m black
ISORT = $(PYTHON) -m isort
SRC_DIR = src
OUTPUT_DIR = data/recordings

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	$(PIP) install -e .

.PHONY: develop
develop:
	$(PIP) install -r dev-requirements.txt
	$(PIP) install -e .

.PHONY: test
test:
	$(PYTEST) --cov=$(SRC_DIR)

.PHONY: quality
quality: lint format

.PHONY: lint
lint:
	$(FLAKE8) $(SRC_DIR)
	$(MYPY) $(SRC_DIR)

.PHONY: format
format:
	$(ISORT) $(SRC_DIR) $(TEST_DIR)
	$(BLACK) $(SRC_DIR) $(TEST_DIR)

.PHONY: check-format
check-format:
	$(ISORT) --check-only $(SRC_DIR) $(TEST_DIR)
	$(BLACK) --check $(SRC_DIR) $(TEST_DIR)

.PHONY: clean
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -name __pycache__ -type d | xargs rm -rf
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.pyd" -delete

.PHONY: run
run:
	@echo "Running noise detector..."
	$(PYTHON) -m src.main

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make install      - Install all dependencies"
	@echo "  make develop      - Install in development mode"
	@echo "  make test         - Run tests"
	@echo "  make quality      - Run all code quality checks and formatting"
	@echo "  make lint         - Run static code analysis"
	@echo "  make format       - Format code to follow standards"
	@echo "  make check-format - Verify code is properly formatted (for CI)"
	@echo "  make clean        - Remove temporary files"
	@echo "  make run          - Run the application"
