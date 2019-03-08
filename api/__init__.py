from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.app_config')

    return app