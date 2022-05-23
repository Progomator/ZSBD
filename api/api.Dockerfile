FROM python:3.8.0

WORKDIR /api

ENV FLASK_APP=WebServer.py
# ENV FLASK_RUN=0.0.0.0

COPY requirements-api.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]