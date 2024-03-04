# controllers/user_controllers/user_sign_up_controller.py

from flask import Blueprint, request, jsonify
import mysql.connector

user_signup_controller = Blueprint('user_signup_controller', __name__)

# now make a folder config at the root of the project, and inside make a file mysql_db.py, instead of connecting mysql db at every controller file
# Assuming you have a MySQL connection already established
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask_tutorial"
)


@user_signup_controller.route('/signup', methods=['POST'])
def create_resource():
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
        cursor.execute("INSERT INTO users (name, email, phone, role, password) VALUES (%s, %s, %s, %s, %s)", (name, email, phone, role, password))
        connection.commit()
        cursor.close()

        # Respond with success message
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500
