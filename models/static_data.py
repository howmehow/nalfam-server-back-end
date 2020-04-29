from utils.db import db
from sqlalchemy.orm import relationship

from models.dynamic_data import DynamicData

class StaticData(db.Model):
    __tablename__ = 'static_data'
    id = db.Column(db.Integer, primary_key = True)
    host_name = db.Column(db.String(255))
    device_type = db.Column(db.String(255))
    operating_system = db.Column(db.String(255))
    mac_address = db.Column(db.String(255), unique=True)
    ip_address = db.Column(db.String(255))
    snap_shots = db.relationship('DynamicData', backref='static_data', lazy=True)

    # def __init__(self, host_name, device_type, operating_system, mac_address, ip_address):
    #     self.host_name = host_name
    #     self.device_type = device_type
    #     self.operating_system = operating_system
    #     self.mac_address = mac_address
    #     self.ip_address = ip_address
        # self.time_stamp

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     child_id = Column(Integer, ForeignKey('child.id'))
#     child = relationship("Child", back_populates="parents")

# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     parents = relationship("Parent", back_populates="child")