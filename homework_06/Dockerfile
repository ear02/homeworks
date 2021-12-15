FROM tiangolo/uwsgi-nginx:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV CONFIG="ProductionConfig"
