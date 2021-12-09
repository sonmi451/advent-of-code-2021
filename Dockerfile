FROM python:3.9 AS app

WORKDIR /submarine

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

COPY . /submarine

FROM app AS test

RUN pytest tests/
