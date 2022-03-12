FROM python:3.9

WORKDIR /etc/evoker

COPY . .

RUN python setup.py install
