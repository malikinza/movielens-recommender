How to reproduce:
1. Install Poetry (if not installed)
2. Run: poetry install
3. Run tests: poetry run python test_surprise.py

## Phase 0 Quickstart (macOS with Poetry)
- Prereqs: Python 3.11, Poetry
- 1) Install dependencies: poetry install
- 2) Generate sample data: make prep
- 3) Run API server (MVP skeleton): uvicorn src.api.app:app --reload --port 8000
- 4) Test endpoints:
  - GET http://localhost:8000/
  - POST http://localhost:8000/recommend with JSON {"user_id": 1, "n": 5}
