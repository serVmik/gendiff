gendiff:
	poetry run gendiff

gendiff-files-json:
	poetry run gendiff filepath1.json filepath2.json

gendiff-files-yml:
	poetry run gendiff filepath1.yml filepath2.yaml

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

test: lint
	poetry run pytest
	poetry run pytest --cov

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck lint test test-coverage

.PHONY: install test lint selfcheck check build gendiff