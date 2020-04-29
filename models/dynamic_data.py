from utils.db import db

class DynamicData(db.Model):
    __tablename__ = 'dynamic_data'
    id = db.Column(db.Integer, primary_key = True)
    static_data_id = db.Column(db.Integer, db.ForeignKey('static_data.id'), nullable=False)
    time_stamp = db.Column(db.String(255))
    upload_speed = db.Column(db.Integer)
    download_speed = db.Column(db.Integer)
    active_connection = db.Column(db.Boolean)



    # def __init__(self, static_id, time_stamp, upload_speed, download_speed, active_connection):
    #     self.static_id = static_id
    #     self.time_stamp = time_stamp
    #     self.upload_speed = upload_speed
    #     self.download_speed = download_speed
    #     self.active_connection = active_connection