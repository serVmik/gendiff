gendiff:
	poetry run gendiff

gendiff-stylish:
	poetry run gendiff_stylish for_developer/file1.json for_developer/file2.json

gendiff-files:
	poetry run gendiff for_developer/file1.json for_developer/file2.json

gendiff-files-json:
	poetry run gendiff for_developer/filepath1.json for_developer/filepath2.json

gendiff-files-yml:
	poetry run gendiff for_developer/filepath1.yml for_developer/filepath2.yaml

gendiff-test:
	poetry run gendiff tests/fixtures/file1_for_test.json tests/fixtures/file2_for_test.json

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
	poetry run pytest -vv
	poetry run pytest --cov

selfcheck:
	poetry check

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: selfcheck lint test test-coverage

.PHONY: install test lint selfcheck check build gendiff