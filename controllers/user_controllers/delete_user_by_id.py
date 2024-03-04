# controllers/user_controllers/delete_user_by_id.py

from flask import Blueprint, jsonify
from config.mysql_db import get_mysql_connection

delete_user_by_id = Blueprint('delete_user_by_id', __name__)

# Add a dynamic route for deleting a single user record based on user ID
@delete_user_by_id.route('/delete-user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Get MySQL database connection
        connection = get_mysql_connection()

        # Query the database to fetch the user record based on user_id
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()  # Fetch the user record

        if user:
            # Execute SQL query to delete user record from the database based on user_id
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            connection.commit()
            cursor.close()

            # Return success message along with deleted user information
            return jsonify({'message': 'User deleted successfully', 'deleted_user': user}), 200
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
