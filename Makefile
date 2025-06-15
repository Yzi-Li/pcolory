.PHONY: refresh lint install test codecov clean

refresh: clean build install lint

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
	pip uninstall -y pcolory
