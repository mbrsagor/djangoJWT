# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install -r requirements.txt
#COPY Pipfile Pipfile.lock /code/
#RUN pipenv install --system

# Copy project
COPY . /code/
