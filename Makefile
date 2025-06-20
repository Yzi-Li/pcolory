.PHONY: refresh build lint install test codecov clean

refresh: clean build lint install test codecov

build:
	python -m build

install:
	pip install .

lint:
	flake8 pcolory/ tests/ --max-line-length=120
	mypy pcolory/ tests/

test:
	make clean
	python -m build
	pip install dist/*.whl
	python -m unittest

codecov:
	coverage run --source pcolory --parallel-mode -m unittest
	coverage combine
	coverage report -m

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf pcolory/__pycache__
	rm -rf build
	rm -rf dist
	rm -rf pcolory.egg-info
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf coverage.xml
	pip uninstall -y pcolory
