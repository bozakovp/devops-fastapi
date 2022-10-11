from flask import Flask

from flask import request

import datetime

import sys

app = Flask(__name__)

@app.route('/')

def hello():

    return "Hello DevOps!"

@app.route('/echo')

def echo():

        sys.stdout.write('there was a request at ' + format(datetime.datetime.now()) + '\n')

        return 'Passed message is {0}'.format(request.args.get('m'))

if __name__ == '__main__':

    app.run(host='0.0.0.0', port='3001')
