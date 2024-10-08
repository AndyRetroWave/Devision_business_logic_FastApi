FROM python:3.11-slim

RUN mkdir /busnes_services

WORKDIR /busnes_services

COPY pyproject.toml .

RUN pip install poetry 
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . . 


