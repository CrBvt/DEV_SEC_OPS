FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

WORKDIR /code/flask_node

#EXPOSE 5000
#
#RUN cd /code/flask_node
#RUN flask run
