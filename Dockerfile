FROM python:3.7-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -U -r /tmp/requirements.txt

COPY *.py ./
COPY librdkafka.config librdkafka.config
COPY users.json users.json
CMD python ./app.py