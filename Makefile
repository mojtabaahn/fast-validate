build:
	python -m build

push:
	python -m twine upload dist/*
