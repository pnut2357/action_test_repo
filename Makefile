pippoetry:
	pip install --upgrade pip && pip install poetry
install:
	poetry install --with dev
test:
	poetry run python -m pytest
format:
	black src/*.py
lint:
	pylint --disable=R,C src/pipeline.py
all: pippoetry install test