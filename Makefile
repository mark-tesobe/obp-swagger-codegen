run:
	poetry run generate

clean:
	poetry run clean

test:
	poetry run pytest

codegen:
	java -jar swagger-codegen-cli-2.4.29.jar generate -o $(path) -i $(source) -l python -c config.json

install:
	poetry install --without tests

setup_install:
	python $(path)/setup.py install

setup_distribution:
	cd $(path); python -m build

setup_twine:
	python -m twine upload -r ${twinerepo} $(path)/dist/*

format: style lint type

style:
	poetry run isort --atomic src tests
	poetry run black src tests

lint:
	poetry run flake8 src tests
	poetry run autoflake  --recursive src tests

type:
	poetry run mypy --strict src tests

path := output
source := https://test.openbankproject.com/obp/v5.0.0/resource-docs/v5.0.0/swagger
twinerepo := pypi
