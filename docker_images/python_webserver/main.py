from flask import Flask
from flask import request
import datetime
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="my-release-mysql.default.svc.cluster.local",
  user="root",
  password="uRVld2EFNH",
)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS pythonweb")
cursor.execute("USE pythonweb")
cursor.execute("CREATE TABLE IF NOT EXISTS requests (message varchar(255), timestamp varchar(255))")
app = Flask(__name__)

@app.route('/')

def hello():

    return "Hello DevOps!"

@app.route('/echo')

def echo():
        sql = "INSERT INTO requests (message, timestamp) VALUES (%s, %s)"
        val = ("test message", format(datetime.datetime.now()))
        cursor.execute(sql, val)
        mydb.commit()
        sys.stderr.write('there was a request at ' + format(datetime.datetime.now()))
        print(cursor.rowcount, "record inserted.")
        return 'there was a request at ' + format(datetime.datetime.now())

if __name__ == '__main__':

    app.run(host='0.0.0.0', port='3001')
