gendiff:
	poetry run gendiff --help

build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv --cov -s
	poetry run flake8 gendiff

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck lint test test-coverage

.PHONY: install test lint selfcheck check build gendiff
