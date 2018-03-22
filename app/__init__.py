from flask import Flask, render_template
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

    migrate = Migrate(app, db)
    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    from .customers import customers as customers_blueprint
    app.register_blueprint(customers_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        # This function handles all 404 error on the app and shows a custom 404
        # error page.
        return render_template('404.html', error=404)

    return app