from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

from flask_migrate import Migrate

db = SQLAlchemy();

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return 'User %s' % username

    migrate = Migrate(app, db)
    from app import models

    return app