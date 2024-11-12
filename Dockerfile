# Base image
FROM python:3.10-slim-bullseye AS base_image

RUN apt-get update && \
  apt-get install -y && \
  apt-get clean -y

WORKDIR /ioet_catalog

COPY ./api ./
COPY ./app ./
COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN pip install poetry && \
  poetry config virtualenvs.create false

# Development image
FROM base_image as dev

RUN poetry install --no-root

CMD ["uvicorn", "api.main:api", "--reload", "--host", "0.0.0.0"]