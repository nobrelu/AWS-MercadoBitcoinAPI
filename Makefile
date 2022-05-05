clean:
	rm -rf .venv day-summary *.checkpoint .pytest_cache .covarage

init: clean
	pip install poetry
	poetry install 