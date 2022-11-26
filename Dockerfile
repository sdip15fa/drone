FROM python:3.10

WORKDIR /app

COPY ./drone ./drone
COPY pyproject.toml poetry.lock LICENSE ./

RUN pip install poetry --no-cache-dir
RUN poetry env use python && poetry install -n && rm -rf ~/.cache/pypoetry/{cache,artifacts}

CMD poetry env use $(poetry env list | tr ' ' '\n' | head -n 1) python3 src/index.py
