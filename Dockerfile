# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /SWE573_Project
EXPOSE 8000

# install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies

COPY requirements.txt /SWE573_Project/
RUN pip install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN pip install -r requirements.txt
# copy project
COPY . /SWE573_Project/
CMD python manage.py makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0:8000