FROM python:3.10.2-slim
ADD . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT python app.py