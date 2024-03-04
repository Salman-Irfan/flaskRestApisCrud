# controllers/user_controllers/user_sign_up_controller.py

from flask import Blueprint, jsonify

user_signup_controller = Blueprint('user_signup_controller', __name__)

@user_signup_controller.route('/signup', methods=['POST'])
def create_resource():
    # Your logic to handle POST request
    data = {
        'message': 'user created successfully'
    }
    return jsonify(data)
