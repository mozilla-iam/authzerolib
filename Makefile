all:
	@echo Hi? Maybe you meant to \`make pypi\`!

pypi:
	python setup.py sdist check upload --sign

test:
	python -m unittest discover tests
