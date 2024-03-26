from flask import Blueprint, jsonify
import numpy as np  # Import NumPy

read_numpy_controller = Blueprint("read_numpy_controller", __name__)


@read_numpy_controller.route("/read-numpy", methods=["GET"])
def read_all_users():
    try:
        # Create a NumPy array
        numpy_array = np.array([1, 2, 3, 4, 5])

        # Convert the NumPy array to a Python list (optional)
        python_list = numpy_array.tolist()

        # Send the array in JSON format as the response
        return jsonify({"numpy_array": python_list}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500
