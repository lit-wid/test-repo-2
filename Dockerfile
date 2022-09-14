FROM python:3.10.2-slim
ADD . /app
COPY ./app/config.py ./
WORKDIR /app
RUN pip install flask \
    pip install mysql-connector-python
ENTRYPOINT python app.py