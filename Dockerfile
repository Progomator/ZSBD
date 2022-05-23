FROM python:3.8.0-alpine

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
