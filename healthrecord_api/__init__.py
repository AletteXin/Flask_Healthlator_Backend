from app import app
from flask_cors import CORS
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from healthrecord_api.blueprints.records.views import records_api_blueprint
from healthrecord_api.blueprints.user.views import users_api_blueprint

app.register_blueprint(records_api_blueprint, url_prefix='/api/records')
app.register_blueprint(users_api_blueprint, url_prefix='/api/user')

@app.route("/")
def home():
    return "hello"

