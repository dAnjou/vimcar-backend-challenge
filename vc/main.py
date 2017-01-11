import click

from vc import create_app
from vc.database import db
from vc.auth.models import User
from vc.cars.models import Car

app = create_app()

@app.cli.command()
def initdb():  # pragma: no cover
    db.create_all()

@app.cli.command()
def dropdb():  # pragma: no cover
    db.drop_all()

@app.cli.command()
def populatedb():  # pragma: no cover
    u1 = User("max", "foo")
    u1.confirmed = True
    db.session.add(u1)
    db.session.add(User("moritz", "bar"))
    db.session.add(Car("A-1", "Ford"))
    db.session.add(Car("A-2", "Opel"))
    db.session.add(Car("B-1", "BMW"))
    db.session.commit()
