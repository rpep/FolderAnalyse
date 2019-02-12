# Upload to PyPi

all:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf __pycache__
	rm -rf dist
	rm -rf *~
	rm -rf *.egg-info