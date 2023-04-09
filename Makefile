gendiff:
	poetry run gendiff

gendiff-files-json:
	poetry run gendiff filepath1.json filepath2.json

gendiff-files-yml:
	poetry run gendiff filepath1.yml filepath2.yaml

gendiff-files-from-test:
	poetry run gendiff tests/fixtures/file1_for_test.json tests/fixtures/file2_for_test.json

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

selfcheck:
	poetry check

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck lint test test-coverage

.PHONY: install test lint selfcheck check build gendiff