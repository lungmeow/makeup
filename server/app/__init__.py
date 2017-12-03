# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    # create and config app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # init
    db.init_app(app)

    # register blue print
    from app.api.v1 import api_v1 as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint)

    return app
