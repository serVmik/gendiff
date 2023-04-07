gendiff:
	poetry run gendiff

gendiff-files:
	poetry run gendiff file1.json file2.json

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

check: selfcheck test lint
