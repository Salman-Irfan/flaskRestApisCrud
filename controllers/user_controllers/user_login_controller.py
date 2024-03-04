# controllers/user_controllers/user_login_controller.py

from flask import Blueprint, jsonify

user_login_controller = Blueprint('user_login_controller', __name__)

@user_login_controller.route('/api/v1/login', methods=['POST'])
def login():
    # Your logic to handle login POST request
    return jsonify({'message': 'Login successful'})