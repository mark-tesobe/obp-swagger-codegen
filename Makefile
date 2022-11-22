run:
	poetry run generate
test:
	poetry run pytest
install:
	poetry install --without tests
format: style lint type

style:
	poetry run isort --atomic src tests
	poetry run black src tests

lint:
	poetry run flake8 src tests
	poetry run autoflake  --recursive src tests

type:
	poetry run mypy --strict src tests
