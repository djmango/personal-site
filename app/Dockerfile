FROM python:3.7-slim-buster

LABEL maintainer='djmango'

WORKDIR  /app

# get app and public env file
COPY . .

# get python packages
RUN pip --no-cache install -r ./requirements/prod.txt

# set envs
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0
ENV FLASK_APP=autoapp.py
ENV DATABASE_URL="sqlite:////tmp/dev.db"

# initialize and build
RUN flask db init && \
    flask db migrate && \
    flask db upgrade

# prepare for run
EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]
# ENTRYPOINT [ "flask", "run" ]