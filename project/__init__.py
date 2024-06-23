from flask import Flask, g
from pymongo import MongoClient
from celery import Celery
from project.config import Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.before_request
    def before_request():
        g.mongo_client = MongoClient('mongodb://localhost:27017')
        g.db = g.mongo_client.video_management

    @app.teardown_request
    def teardown_request(exception=None):
        if hasattr(g, 'mongo_client'):
            g.mongo_client.close()

    from project.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    celery.conf.update(app.config)
    return app

