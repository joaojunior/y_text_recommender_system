clean:
	find . -name '*.pyc' -delete
	find . -name '*.swp' -delete
	rm -rf .coverage
	rm -rf MANIFEST
	rm -rf .tox/

test: clean
	tox

api: clean
	python setup.py install
	pip install -r requirements-api.txt
	export FLASK_APP=api/app.py && flask run
