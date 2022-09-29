FROM alpine:latest
WORKDIR /devops
COPY ./requirements.txt /devops
COPY ./main.py /devops

RUN apk update
RUN apk add py3-pip
RUN pip install -r /devops/requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
