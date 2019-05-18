FROM python:3.7
WORKDIR /root
RUN pip install --upgrade pip
RUN pip install pika
RUN pip install flask
CMD export FLASK_APP=api.py && flask run --host=0.0.0.0