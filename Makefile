all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]].*:' Makefile

upload: dist
	python setup.py check upload --sign

test:
	flake8 . --exclude=venv/*
	python -m unittest discover tests

dist: build
	python setup.py sdist

build:
	python setup.py build

install: build
	python setup.py install

install_test_requirements:
	pip install -r test_requirements.txt

venv: venv
	python -m venv venv
	@echo Run \`source venv/bin/activate\`

clean:
	rm -fr __pycache__/ tests/__pycache__/
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info/

