install:
	poetry install --with dev
test:
	poetry run python -m pytest
format:
	black src/*.py
lint:
	pylint --disable=R,C src/pipeline.py
all: install test