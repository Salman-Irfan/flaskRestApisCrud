from flask import Blueprint, jsonify
import pandas as pd  # Import pandas

make_pandas_controller = Blueprint("make_pandas_controller", __name__)

@make_pandas_controller.route("/api-pandas", methods=["GET"])

def read_all_users():
    try:
        return jsonify({"pandas_data": "pandas_data"}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500
