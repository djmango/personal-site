FROM node:12.4-alpine

LABEL maintainer='djmango'

WORKDIR /webpack/

COPY . .

RUN npm install --no-progress --ignore-optional

EXPOSE 2992

# CMD npm run build
CMD npm run webpack-dev-server