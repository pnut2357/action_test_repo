pippoetry:
	pip install --upgrade pip && pip install poetry
venv:
	poetry shell
install:
	poetry install --with dev
test:
	poetry run python -m pytest -vv --cov=src
format:
	black ./src/*.py
lint:
	pylint --disable=R,C ./src/pipeline.py
all: pippoetry install test