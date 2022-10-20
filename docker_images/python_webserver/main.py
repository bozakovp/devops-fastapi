from flask import Flask
from flask import request
import datetime
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="my-release-mysql.default.svc.cluster.local",
  user="root",
  password="uRVld2EFNH",
  database="pythonweb"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/')

def hello():

    return "Hello DevOps!"

@app.route('/echo')

def echo():
        sql = "INSERT INTO requests (message, timestamp) VALUES (%s, %s)"
        val = ("test message", format(datetime.datetime.now()))
        mycursor.execute(sql, val)
        mydb.commit()
        sys.stderr.write('there was a request at ' + format(datetime.datetime.now()))
        print(mycursor.rowcount, "record inserted.")
        return 'there was a request at ' + format(datetime.datetime.now())

if __name__ == '__main__':

    app.run(host='0.0.0.0', port='3001')
