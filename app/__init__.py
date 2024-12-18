import logging
import os
from flask import Flask, Blueprint
from dotenv import load_dotenv
from app.api import api
from app.extensions import db, migrate
from app.config import Config
from app.models import register_models
from app.modules.chain.namespace import namespace as chain_namespace
from app.modules.transaction.namspace import namespace as transaction_namespace
from app.modules.mining.namespace import namespace as mining_namespace


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
    flask_app.config['RESTPLUS_ERROR_404_HELP'] = False


def create_app():
    load_dotenv()

    flask_app = Flask(__name__)

    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    register_models()

    if os.getenv("FLASK_ENV") == 'development':
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    return flask_app


def register_blueprints(flask_app):
    blueprint = Blueprint('main', __name__, url_prefix='/api/pycoinlab')

    api.init_app(blueprint)

    api.add_namespace(chain_namespace)
    api.add_namespace(transaction_namespace)
    api.add_namespace(mining_namespace)

    flask_app.register_blueprint(blueprint)


app = create_app()

register_blueprints(app)
configure_app(app)


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)
