FROM python:3.10

WORKDIR /app

COPY ./src ./src
COPY pyproject.toml LICENSE ./

RUN pip install poetry
RUN python -m poetry env use python && python -m poetry install

CMD python3 src/index.py
