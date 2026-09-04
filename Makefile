UV ?= uv
SRC_DIR = src
OUTPUT_DIR = data/recordings

.PHONY: install
install:
	$(UV) sync --no-dev

.PHONY: develop
develop:
	$(UV) sync --all-groups

.PHONY: test
test:
	$(UV) run pytest --cov=$(SRC_DIR)

.PHONY: quality
quality: lint format

.PHONY: lint
lint:
	$(UV) run ruff check $(SRC_DIR)
	$(UV) run mypy $(SRC_DIR)

.PHONY: format
format:
	$(UV) run ruff check --fix $(SRC_DIR)
	$(UV) run ruff format $(SRC_DIR)

.PHONY: check-format
check-format:
	$(UV) run ruff check $(SRC_DIR)
	$(UV) run ruff format --check $(SRC_DIR)

.PHONY: clean
clean:
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .mypy_cache/
	find . -name __pycache__ -type d | xargs rm -rf
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name "*.pyd" -delete

.PHONY: run
run:
	@echo "Running noise detector..."
	$(UV) run python -m src.main

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make develop      - Install all dependencies (including dev)"
	@echo "  make test         - Run tests"
	@echo "  make quality      - Run all code quality checks and formatting"
	@echo "  make lint         - Run static code analysis"
	@echo "  make format       - Format code to follow standards"
	@echo "  make check-format - Verify code is properly formatted (for CI)"
	@echo "  make clean        - Remove temporary files"
	@echo "  make run          - Run the application"
