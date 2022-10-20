FROM alpine:latest
WORKDIR /devops
COPY ./requirements.txt /devops
COPY ./main.py /devops

RUN apk update
RUN apk add py3-pip
RUN pip install -r /devops/requirements.txt
RUN pip install mysql-connector-python
CMD ["python3", "/devops/main.py"]
