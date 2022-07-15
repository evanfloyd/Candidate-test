FROM python:3.9.5

EXPOSE 5000

ADD main.py .

RUN pip install flask prometheus_client werkzeug

CMD [ "python", "./main.py" ]