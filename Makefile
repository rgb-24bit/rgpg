pep8:
	flake8 --ignore=E501,F401,E128,E402,E731,F821 rgpg

test:
	py.test -s --tb=short

install:
	python setup.py install
