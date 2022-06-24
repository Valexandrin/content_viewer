-include .env
export

run:
	@python -m frontend

lint:
	@mypy frontend
	@flake8 frontend
