FROM python:3.9.5

WORKDIR /app
COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]