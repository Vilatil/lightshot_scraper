FROM python:3.10-alpine

ARG DB_HOST
ARG DB_USER
ARG DB_DATABASE
ARG DB_PASSWORD

ENV DB_HOST=${DB_HOST}
ENV DB_USER=${DB_USER}
ENV DB_DATABASE=${DB_DATABASE}
ENV DB_PASSWORD=${DB_PASSWORD}

WORKDIR /lightshot_scraper
COPY requirements.txt .
RUN apk add --no-cache libxml2-dev libxslt-dev gcc build-base \
        && pip3 install --no-cache lxml
COPY requirements.txt .
RUN pip3 install --no-cache -Ur requirements.txt
EXPOSE 3306
COPY . .
ENTRYPOINT ["top"]


