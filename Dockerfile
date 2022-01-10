# syntax=docker/dockerfile:1
FROM python:3.10.0-alpine3.15
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /SWE573_Project
EXPOSE 8000

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
CMD python manage.py makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0:8000