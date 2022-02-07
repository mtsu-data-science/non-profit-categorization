install-precommit:
	pre-commit install

install-virtualenv:
	poetry install

poetry-lock:
	poetry lock

poetry-add:
	poetry add $(package)

poetry-remove:
	poetry remove $(package)