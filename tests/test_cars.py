import json

import pytest
from freezegun import freeze_time

from vc.database import db
from vc.cars.models import Car
from vc.auth.models import User

@freeze_time("2017-01-11 13:20")
def test_cars_with_jwt(client):
    db.session.add(User("max", "foobar"))
    cars = sorted([
        ("lorem", "Opel"),
        ("ipsum", "BMW"),
        ("dolor", "Ford")
    ])
    for car in cars:
        db.session.add(Car(*car))
    db.session.commit()
    jwt = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE0ODQxNDA3MTIsImV4cC"
           "I6MTQ4NDE0MTAxMiwibmJmIjoxNDg0MTQwNzEyLCJpZGVudGl0eSI6MX0.0Cp4qTYcb"
           "tOs7fx-vlvWxlrxdTR7HoX2ipyMwkul2mc")
    response = client.get('/cars/', headers=[('Authorization', 'JWT %s' % jwt)])
    assert response.status_code == 200
    expected = []
    for car in json.loads(response.data.decode('utf-8')):
        expected.append((car['identifier'], car['brand']))
    assert sorted(expected) == cars

def test_cars_without_jwt(client):
    response = client.get('/cars/')
    assert response.status_code == 401
