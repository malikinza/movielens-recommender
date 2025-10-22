.PHONY: install prep serve test

install:
	poetry install

prep:
	python src/data_prep.py

serve:
	uvicorn src.api.app:app --reload --port 8000

test:
	@echo "No tests yet. Add tests under tests/"

