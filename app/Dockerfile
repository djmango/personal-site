FROM python:3.7-slim-buster

LABEL maintainer='djmango'

WORKDIR  /app

# get app and public export file
COPY requirements/ ./requirements/
VOLUME [ "./assets/:/app/assets/" ]
COPY app.py ./
COPY personalWebsiteFlask/ ./personalWebsiteFlask/
COPY *.env ./

# get python packages
RUN pip --no-cache install -r requirements/prod.txt

# set exports
RUN export FLASK_export="production" && \
    export FLASK_DEBUG="0" && \
    export FLASK_APP="app.py" && \
    export DATABASE_URL="sqlite://"

# initialize and build
RUN flask db init && \
    flask db migrate && \
    flask db upgrade

# prepare for run
EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]