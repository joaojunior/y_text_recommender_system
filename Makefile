clean:
	find . -name '*.pyc' -delete
	find . -name '*.swp' -delete
	rm -rf .coverage
	rm -rf MANIFEST
	rm -rf .tox/

test: clean
	tox
