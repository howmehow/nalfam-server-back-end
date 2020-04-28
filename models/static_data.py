import random
from utils.db import db

class StaticData(db.Model):
    __tablename__ = 'static_data'
    id = db.Column(db.Integer, primary_key = True)
    host_name = db.Column(db.String(255))
    device_type = db.Column(db.String(255))
    operating_system = db.Column(db.String(255))
    mac_address = db.Column(db.String(255), unique=True)
    ip_address = db.Column(db.String(255))

    def __init__(self, host_name, device_type, operating_system, mac_address, ip_address):
        self.host_name = host_name
        self.device_type = device_type
        self.operating_system = operating_system
        self.mac_address = mac_address
        self.ip_address = ip_address