# controllers/user_controllers/get_user_by_id.py

from flask import Blueprint, jsonify
from config.mysql_db import get_mysql_connection

get_user_by_id = Blueprint('get_user_by_id', __name__)

# Add a dynamic route for fetching a single user record based on user ID
@get_user_by_id.route('/users/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    try:
        # Get MySQL database connection
        connection = get_mysql_connection()

        # Query the database to fetch the user record based on user_id
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()  # Fetch the first user record
        cursor.close()

        if user:
            # Return the user record as JSON response
            return jsonify(user), 200
        else:
            # If no user found with the provided user_id, return 404 Not Found
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        # Handle any exceptions and return 500 Internal Server Error
        return jsonify({'error': str(e)}), 500
    finally:
        # Close the database connection
        if connection:
            connection.close()
