FROM python:3.6-alpine

RUN apk add --update --no-cache curl jq python3 py3-pip pkgconfig

ADD ./requirements.txt /opt/webapp-get-pods/

# k8s 1.29 bug workaround
# WORKDIR /opt/webapp-get-pods

RUN cd /opt/webapp-get-pods && pip3 install -r requirements.txt

ADD . /opt/webapp-get-pods

EXPOSE 8080

ENTRYPOINT ["python3", "/opt/webapp-get-pods/app.py"]
