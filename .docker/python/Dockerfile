FROM python:3.7-slim-stretch

COPY ./requirements.txt /tmp/requirements.txt

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
    && pip install -U pip setuptools wheel \
    && pip install -r /tmp/requirements.txt \
    && apt-get autoremove -yqq --purge \
    && apt-get clean

RUN pip install -r /tmp/requirements.txt

ENV PYTHONPATH /code

WORKDIR /code
CMD ["bash"]
