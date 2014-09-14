test: pep8 test_server

pep8:
	pep8 serialized_redis

test_server:
	python -m unittest test.py
