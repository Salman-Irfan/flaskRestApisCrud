# controllers/user_controllers/read_all_users_controller.py

from flask import Blueprint, jsonify
from config.mysql_db import get_mysql_connection

read_all_users_controller = Blueprint('read_all_users_controller', __name__)

@read_all_users_controller.route('/all-users', methods=['GET'])

def read_all_users():
    try:
        connection = get_mysql_connection()
        cursor = connection.cursor(dictionary=True)

        # Execute the SQL query to fetch all users
        cursor.execute("SELECT * FROM users")

        # Fetch all users
        users = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Return the users as JSON response
        return jsonify(users), 200
    except Exception as e:
        # Handle errors
        return jsonify({'error': str(e)}), 500
