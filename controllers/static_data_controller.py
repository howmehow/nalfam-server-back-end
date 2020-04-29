from flask import Blueprint, request, jsonify, Response
from sqlalchemy import update

from utils.db import db
from models.static_data import StaticData
from models.dynamic_data import DynamicData
from schemas.static_data_schema import static_data_schema
from schemas.dynamic_data_schema import dynamic_data_schema

static_data_blueprint = Blueprint('static_data_blueprint', __name__)

@static_data_blueprint.route('/', methods=['GET'])
def get_static_data():
    data = StaticData.query.all()
    result = static_data_schema.dumps(data)
    response = Response(result, status=200, mimetype='application/json')
    return response

@static_data_blueprint.route('/dynamic-data', methods=['GET'])
def get_dynamic_data():
    data = DynamicData.query.all()
    result = dynamic_data_schema.dumps(data)
    response = Response(result, status=200, mimetype='application/json')
    return response