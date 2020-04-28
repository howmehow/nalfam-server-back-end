from utils.ma import ma
from models.static_data import StaticData

class StaticDataSchema(ma.Schema):
    class Meta:
        fields = ('id','host_name', 'device_type', 'operating_system', 'mac_address', 'ip_address')

static_data_schema = StaticDataSchema(many=True)