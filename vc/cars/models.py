from vc.database import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(100))
    brand = db.Column(db.String(300))

    def __init__(self, identifier, brand):
        self.identifier = identifier
        self.brand = brand

    def as_dict(self):
        return {
            "id": self.id,
            "identifier": self.identifier,
            "brand": self.brand
        }

    def __repr__(self):  # pragma: no cover
        return '<Car %r>' % self.identifier
