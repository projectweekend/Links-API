FROM python:2

RUN apt-get update -qq

RUN mkdir /code
ADD . /code/
WORKDIR /code

RUN pip install -r requirements.txt

WORKDIR /code/links

EXPOSE 5000
