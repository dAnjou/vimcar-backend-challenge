from flask import Flask
from flask_jwt import JWT

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_AUTH_URL_RULE'] = '/auth/login'
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

    from vc.database import db
    db.init_app(app)

    from vc.auth import authenticate, identity
    jwt = JWT(app, authenticate, identity)

    from vc.cars import cars
    from vc.auth import auth
    app.register_blueprint(cars, url_prefix='/cars')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
