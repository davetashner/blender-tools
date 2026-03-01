.PHONY: test lint format typecheck check

test:
	pytest --cov --cov-report=term-missing --cov-fail-under=95

lint:
	ruff check src/ tests/
	ruff format --check src/ tests/

format:
	ruff format src/ tests/

typecheck:
	mypy src/

check: lint typecheck test
