install:
	poetry install --with dev && poetry lock
test:
	poetry run python -m pytest
format:
	black *.py
lint:
	pylint --disable=R,C hello.py
all: install test