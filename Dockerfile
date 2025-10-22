FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install --no-cache-dir --upgrade pip
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
COPY . /app
RUN poetry install --no-dev
EXPOSE 8000
CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]

