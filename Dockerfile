FROM python:3.7

MAINTAINER Ker Helium keepthethink@hotmail.com

ADD . /app

RUN cd /app && pip3 install -r requirements.txt && apt-get install graphviz

CMD python3 main.py
