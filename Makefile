all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]].*:' Makefile

pypi:
	python setup.py sdist check upload --sign

test:
	flake8 . --exclude=venv/*
	python -m unittest discover tests
