from flask import Flask


def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes.planet import planet_bp
    app.register_blueprint(planet_bp)
    
    return app
