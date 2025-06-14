build:
	python -m build

lint:
	flake8 pcolory/ tests/ --max-line-length=120
	mypy pcolory/ tests/

test:
	python -m unittest