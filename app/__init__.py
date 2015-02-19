from flask import Flask, jsonify, render_template, Response
from pymongo import MongoClient

app = Flask(__name__)

app.config.from_object('config.app_config')

from data.controllers import data as data_module
app.register_blueprint(data_module)

@app.route("/")
def index():
  return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
  return "Page not found"

@app.errorhandler(500)
def internal_server_error(error):
  return "Something went wrong"
