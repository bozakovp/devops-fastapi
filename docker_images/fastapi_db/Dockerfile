FROM python:3.8
WORKDIR /devops
COPY ./requirements.txt /devops
COPY ./sql_app /devops/sql_app

RUN pip install -r /devops/requirements.txt
RUN pip install SQLAlchemy
CMD uvicorn sql_app.main:app --host 0.0.0.0 --port 8080 --workers 4
