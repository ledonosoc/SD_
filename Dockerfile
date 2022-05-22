FROM python:3.7-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -U -r /tmp/requirements.txt

COPY *.py ./
COPY librdkafka.config librdkafka.config
CMD python ./API_blocked.py -f ./librdkafka.config -t tarea1