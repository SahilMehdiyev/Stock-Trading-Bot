PYTHON := python3
MANAGE := $(PYTHON) src/manage.py

.PHONY: run migrate makemigrations shell createsuperuser test collectstatic

run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

shell:
	$(MANAGE) shell

createsuperuser:
	$(MANAGE) createsuperuser

test:
	$(MANAGE) test

collectstatic:
	$(MANAGE) collectstatic --noinput
