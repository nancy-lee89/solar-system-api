from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')


    from app.models.planet import Planet

    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes.planet import planet_bp
    app.register_blueprint(planet_bp)
    
    return app
