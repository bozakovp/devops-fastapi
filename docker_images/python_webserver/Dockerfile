FROM alpine:latest
WORKDIR /devops
COPY ./requirements.txt /devops
COPY ./main.py /devops

RUN apk update
RUN apk add py3-pip
RUN pip install -r /devops/requirements.txt
CMD ["python3", "/devops/main.py"]
