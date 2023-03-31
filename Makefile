gendiff:
	poetry run gendiff

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
