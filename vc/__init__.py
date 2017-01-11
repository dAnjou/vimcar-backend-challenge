from flask import Flask
from flask_jwt import JWT

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_AUTH_URL_RULE'] = '/auth/login'
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    app.config.from_envvar('VC_SETTINGS')

    from vc.database import db
    db.init_app(app)

    from vc.auth import auth, jwt_authenticate, jwt_identity
    jwt = JWT(app, jwt_authenticate, jwt_identity)
    app.register_blueprint(auth, url_prefix='/auth')

    from vc.cars import cars
    app.register_blueprint(cars, url_prefix='/cars')

    return app
