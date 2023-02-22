FROM python:3.10.4

ENV PYTHONUNBUFFERED 1 
EXPOSE 8000
WORKDIR /src

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false

COPY ./src/pyproject.toml ./src/poetry.lock ./src/alembic.ini ./src/migrations/ /src/

RUN poetry install

RUN apt-get update && apt-get install -y postgresql-client

COPY ./src /src

# RUN alembic upgrade head

CMD ["poetry", "run", "start"]
