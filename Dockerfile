FROM ubuntu:18.04

LABEL maintainer='djmango'

# get ubuntu packages
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev npm webpack

ADD ./requirements/prod.txt /requirements.txt

# get python packages
RUN pip3 install -r requirements.txt

# get app and public env file
COPY . /

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
    flask db upgrade && \
    npm install && \
    npm run build

# prepare for run
EXPOSE 5000
ENTRYPOINT gunicorn personalWebsiteFlask.app:create_app\(\) -b 0.0.0.0:5000 -w 3