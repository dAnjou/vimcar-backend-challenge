from passlib.hash import pbkdf2_sha256

from vc.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    confirmed = db.Column(db.Boolean, default=False)

    def __init__(self, email, password):
        self.email = email
        self.password = pbkdf2_sha256.hash(password)

    def __repr__(self):
        return '<User %r>' % self.email
