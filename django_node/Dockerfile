FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV POSTGRES_NAME=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]