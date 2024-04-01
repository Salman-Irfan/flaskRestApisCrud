from flask import Blueprint, jsonify, request
import pandas as pd

make_pandas_controller = Blueprint("make_pandas_controller", __name__)


@make_pandas_controller.route("/pandas-series", methods=["POST"])
def create_pandas_series():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract the list from the JSON data
        # In the line data_list = data.get("data", []), we passed an empty array [] as the default value to the data.get() function. This is done as a precautionary measure to handle cases where the JSON data may not contain the "data" key or if it is missing.
        data_list = data.get("data", [])

        # Create a Pandas Series from the list
        series = pd.Series(data_list)
        print(series)
        # Convert the Pandas Series to a dictionary for JSON serialization
        series_dict = series.to_dict()

        # Return the Pandas Series as JSON response
        return jsonify({"pandas_series": series_dict}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500


# make another api that makes series and also with its dtype and name
@make_pandas_controller.route("/pandas-series-with-dtype", methods=["POST"])
def create_pandas_series_with_dtype():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract the list from the JSON data
        data_list = data.get("data", [])

        # Extract dtype and name from JSON data
        dtype = data.get("dtype", None)
        name = data.get("name", None)

        # Create a Pandas Series with specified dtype and name
        series = pd.Series(data_list, dtype=dtype, name=name)
        print(series)
        # Convert the Pandas Series to a dictionary for JSON serialization
        series_dict = series.to_dict()

        # Return the Pandas Series as JSON response
        return jsonify({"pandas_series": series_dict}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500
