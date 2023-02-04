FROM python:3.10-alpine

WORKDIR /app

COPY ./drone ./drone
COPY pyproject.toml poetry.lock LICENSE ./

RUN apk add curl && curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false && poetry install -n && rm -rf ~/.cache/pypoetry/{cache,artifacts}

CMD python3 src/index.py
