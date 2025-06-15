all: build lint test codecov

build:
	python -m build

lint:
	flake8 pcolory/ tests/ --max-line-length=120
	mypy pcolory/ tests/

test:
	python -m unittest

codecov:
	coverage run --source pcolory --parallel-mode -m unittest
	coverage combine
	coverage report -m
