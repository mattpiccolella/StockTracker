from flask import Blueprint, Response, jsonify, url_for
from pymongo import MongoClient
import json, datetime

data = Blueprint('data', __name__, url_prefix='/data')

@data.route("/")
def hello():
  return "This is my first data!"
