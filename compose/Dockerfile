FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
WORKDIR /app

EXPOSE 8000

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - cognito_drf.wsgi:application
