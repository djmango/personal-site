FROM python:3.6-slim

LABEL maintainer='djmango'

WORKDIR /app/

# get app and public env file
COPY . .
#TODO: only copy the neccesary stuff for prod

# get python packages
RUN pip3 install -r ./requirements/prod.txt

# set envs
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_APP=autoapp.py
ENV DATABASE_URL="sqlite:///dev.db"

# initialize and build during run, otherwise build is not there
# prepare for run
EXPOSE 5000
CMD start.sh