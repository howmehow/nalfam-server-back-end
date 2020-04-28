import requests
import json
from flask import Blueprint, request, jsonify, Response
from sqlalchemy import update

from models.static_data import StaticData
from schemas.static_data_schema import static_data_schema
from utils.db import db

refresh_blueprint = Blueprint('refresh_blueprint', __name__)

@refresh_blueprint.route('/', methods=['GET'])
def get_shit_done():
    fetch = requests.get('http://localhost:5000/devices/')
    devices = fetch.json()
    for device in devices:
        del device["id"]
        del device["active_connection"]
        del device["upload_speed"]
        del device["download_speed"]

        static_data = StaticData(**device)
        db.session.add(static_data)

    db.session.commit()
    
    return jsonify({"Shit got": "done"})
