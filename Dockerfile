FROM python:3.6-alpine

RUN apk add --update --no-cache curl jq python3 py3-pip

ADD ./requirements.txt /opt/webapp-get-pods/

WORKDIR /opt/webapp-get-pods

RUN pip3 install -r requirements.txt

ADD . /opt/webapp-get-pods

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]

