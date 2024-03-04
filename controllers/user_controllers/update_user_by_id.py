# controllers/user_controllers/update_user_by_id.py

from flask import Blueprint, jsonify, request
from config.mysql_db import get_mysql_connection

update_user_by_id = Blueprint("update_user_by_id", __name__)


# Add a dynamic route for updating a single user record based on user ID
@update_user_by_id.route("/update-user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        # Get MySQL database connection
        connection = get_mysql_connection()

        # Get the updated user data from the request
        data = request.json
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        role = data.get("role")
        password = data.get("password")

        # Check if the user exists
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()

        if user:
            # Execute SQL query to update user record in the database based on user_id
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE users SET name = %s, email = %s, phone = %s, role = %s, password = %s WHERE id = %s",
                (name, email, phone, role, password, user_id),
            )
            connection.commit()
            cursor.close()

            # Return success message along with updated user information
            return (
                jsonify(
                    {
                        "message": "User updated successfully",
                        "updated_user": {
                            "id": user_id,
                            "name": name,
                            "email": email,
                            "phone": phone,
                            "role": role,
                            "password": password,
                        },
                    }
                ),
                200,
            )
        else:
            # If no user found with the provided user_id, return 404 Not Found
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        # Handle any exceptions and return 500 Internal Server Error
        return jsonify({"error": str(e)}), 500
    finally:
        # Close the database connection
        if connection:
            connection.close()
