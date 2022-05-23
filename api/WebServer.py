from flask import Flask, request, jsonify
from DB_Connector import db_uri
from flask_sqlalchemy import SQLAlchemy
import os


WebServer = Flask(__name__)
WebServer.config['SQLALCHEMY_DATABASE_URI'] = db_uri
WebServer.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
WebServer.config['SECRET_KEY'] = "secretkey12345"             #TODO: keys from environ
WebServer.config['WTF_CSRF_SECRET_KEY'] = "secretkey12345"

db = SQLAlchemy(WebServer)



if __name__ == "__main__":
    WebServer.run(host="0.0.0.0")


import API


