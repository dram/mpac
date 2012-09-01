man:
	rst2man mpac.rst > mpac.8

.PHONY: tests

tests:
	python tests/tests.py
