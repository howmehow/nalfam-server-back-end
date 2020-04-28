import os

from flask import Flask

from controllers.static_data_controller import static_data_blueprint
from controllers.refresh_controller import refresh_blueprint
from utils.db import db

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(static_data_blueprint, url_prefix='/static-data')
    app.register_blueprint(refresh_blueprint, url_prefix='/refresh')

    return app