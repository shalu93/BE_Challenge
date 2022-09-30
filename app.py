import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name/<name>")
def get_user_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_user_details():
    name=request.args.get('name')
    place=request.args.get('place')
    return "Name : {}, Place: {}".format(name,place)

if __name__ == '__main__':
    app.run()