# controllers/user_controllers/user_sign_up_controller.py

from flask import Blueprint, request, jsonify
from config.mysql_db import get_mysql_connection

user_signup_controller = Blueprint('user_signup_controller', __name__)

# Get MySQL database connection
connection = get_mysql_connection()

@user_signup_controller.route('/signup', methods=['POST'])
def user_sign_up():
    try:
        # Get user data from the request
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        role = data.get('role')
        password = data.get('password')

        # Insert user data into the database
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO users (name, email, phone, role, password) VALUES ('{name}', '{email}', '{phone}', '{role}', '{password}')")
        # for preventing sql injection
        # cursor.execute("INSERT INTO users (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)", (name, email, phone, role, password))
        connection.commit()

        # Fetch the created user's data
        user_id = cursor.lastrowid
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

        cursor.close()

        # Respond with success message and created user data
        response_data = {
            'message': 'User created successfully',
            'user': {
                'id': user_data[0],
                'name': user_data[1],
                'email': user_data[2],
                'phone': user_data[3],
                'role': user_data[4]
                # Add more fields if needed
            }
        }
        return jsonify(response_data), 201
    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500

