# docker build . -t app
# docker run -p 8000:8000 app
FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry


COPY app/pyproject.toml ./

COPY app .

RUN poetry config virtualenvs.create false

RUN poetry install

CMD uvicorn app:app --host=0.0.0.0
