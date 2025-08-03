from flask import Blueprint, request, jsonify
from models.user import User
from models import db
from schemas.user import user_schema, users_schema
from utils.auth import hash_password, verify_password

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.dump(users), 200

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.dump(user), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    data['password'] = hash_password(data['password'])
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201

@user_bp.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        if key == 'password':
            value = hash_password(value)
        setattr(user, key, value)
    db.session.commit()
    return user_schema.dump(user), 200

@user_bp.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Deleted'}, 200