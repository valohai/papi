all: format lint

check-format:
	black --check .
	isort --check .

format:
	black .
	isort .

lint:
	flake8 .
	mypy .
