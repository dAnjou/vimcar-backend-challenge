from flask import Blueprint, jsonify, request, current_app, url_for
from werkzeug.security import safe_str_cmp
from itsdangerous import URLSafeTimedSerializer

from vc.database import db
from vc.auth.models import User

auth = Blueprint('auth', __name__)

def authenticate(email, password):
    user = User.query.filter_by(email=email, confirmed=True).first()
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user = User.query.get(payload['identity'])
    return user

@auth.route('/signup', methods=['POST'])
def signup():
    #TODO: validation!
    payload = request.get_json()
    email = payload['email']
    password = payload['password']
    db.session.add(User(email, password))
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])  #TODO: salt?
    confirm_token = s.dumps({"id": user.id, "email": user.email})
    print(url_for('auth.confirm', token=confirm_token, _external=True))
    return jsonify(result='success')

@auth.route('/confirm')
def confirm():
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])  #TODO: salt?
    payload = s.loads(request.args.get('token', ''))
    uid = payload['id']
    email = payload['email']
    user = User.query.filter_by(id=uid, email=email, confirmed=False).first()
    user.confirmed = True
    db.session.commit()
    return jsonify(result='success')
