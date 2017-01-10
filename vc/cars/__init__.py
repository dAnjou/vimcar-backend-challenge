from flask import Blueprint, jsonify
from flask_jwt import jwt_required

from vc.cars.models import Car

cars = Blueprint('cars', __name__)

@cars.route('/')
@jwt_required()
def list():
    return jsonify([c.as_dict() for c in Car.query.all()])
