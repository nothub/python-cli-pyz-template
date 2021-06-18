# Makefile

.ONESHELL:

all: run

virtualenv: $(eval SHELL:=/bin/bash)
	test -d venv || python3 -m venv venv

requirements: $(eval SHELL:=/bin/bash) virtualenv requirements.txt
	source venv/bin/activate
	pip3 install -r requirements.txt

run: $(eval SHELL:=/bin/bash) requirements
	source venv/bin/activate
	python3 main.py

package: $(eval SHELL:=/bin/bash) requirements
	source venv/bin/activate
	pip3 install zipapps
	python3 -m zipapps -c -a main.py -m main -o app -r requirements.txt -p "/usr/bin/env python3"
