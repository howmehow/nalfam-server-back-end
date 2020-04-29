import requests
import json
from flask import Blueprint, request, jsonify, Response
from sqlalchemy import update
from datetime import datetime

from models.static_data import StaticData
from models.dynamic_data import DynamicData
from schemas.static_data_schema import static_data_schema
from utils.db import db

refresh_blueprint = Blueprint('refresh_blueprint', __name__)

@refresh_blueprint.route('/', methods=['GET'])
def get_shit_done():
    fetch = requests.get('http://localhost:5000/devices/')
    devices = fetch.json()
    for device in devices:
        del device["id"]
        active = device.pop("active_connection")
        upload = device.pop("upload_speed")
        download = device.pop("download_speed")

        # StaticData.query.all()
        # if device["mac_address"] == 
        static_data = StaticData(**device)
        db.session.add(static_data)
        db.session.commit()

        snapshot = {"static_data_id":static_data.id, "time_stamp": datetime.now(), "active_connection":active, "upload_speed":upload, "download_speed":download}
        dynamic_data = DynamicData(**snapshot)
        db.session.add(dynamic_data)
        db.session.commit()

    
    
    return jsonify({"Shit got": "done"})
