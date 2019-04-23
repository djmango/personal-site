FROM ubuntu:18.04

LABEL maintainer='djmango'

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev npm webpack

COPY ./requirements/prod.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app
COPY .env /app

RUN export LC_ALL=C.UTF-8 && \
    export LANG=C.UTF-8 && \
    flask db init && \
    flask db migrate && \
    flask db upgrade && \
    export FLASK_ENV=production && \
    export FLASK_DEBUG=0 && \
    npm install && \
    npm run build

# ENTRYPOINT [ "python" ]

CMD ["flask run"]