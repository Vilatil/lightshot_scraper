FROM python:3.10-alpine

WORKDIR /lightshot_scraper
COPY requirements.txt .
RUN apk add --no-cache libxml2-dev libxslt-dev gcc build-base \
        && pip3 install --no-cache lxml
COPY requirements.txt .
RUN pip3 install --no-cache -Ur requirements.txt
COPY . .
ENTRYPOINT ["top"]


