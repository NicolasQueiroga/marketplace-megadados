# pull the official docker image
FROM python:3.9.4-slim
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /api

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .