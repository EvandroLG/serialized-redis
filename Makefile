test: pep8 test_server

pep8:
	pep8 serialized_redis.py

test_server:
	python -m unittest test.py
