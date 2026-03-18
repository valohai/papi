all: format lint

check-format:
	ruff format --check .
	ruff check --select I --diff .

format:
	ruff format .
	ruff check --select I --fix .

lint:
	ruff check .
	mypy .
