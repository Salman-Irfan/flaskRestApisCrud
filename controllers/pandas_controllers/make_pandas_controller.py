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


# make api that makes pandas series from a dictionary
@make_pandas_controller.route("/pandas-series-from-dict", methods=["POST"])
def create_pandas_series_from_dict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract the dictionary from the JSON data
        data_dict = data.get("data", {})

        # Create a Pandas Series from the dictionary
        series = pd.Series(data_dict)
        print(series)
        # Convert the Pandas Series to a dictionary for JSON serialization
        series_dict = series.to_dict()

        # Return the Pandas Series as JSON response
        return jsonify({"pandas_series": series_dict}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500


# make an api controller that makes patyon data frame from a list
@make_pandas_controller.route("/pandas-dataframe", methods=["POST"])
def create_pandas_dataframe():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract the list of dictionaries from the JSON data
        data_list = data.get("data", [])

        # Create a Pandas DataFrame from the list of dictionaries
        df = pd.DataFrame(data_list)
        print(df)
        # Convert the Pandas DataFrame to a dictionary for JSON serialization
        df_dict = df.to_dict(orient="records")

        # Return the Pandas DataFrame as JSON response
        return jsonify({"pandas_dataframe": df_dict}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500


# make an api to insert a new data in data frame
@make_pandas_controller.route("/insert-data", methods=["POST"])
def insert_data():
    try:
        # Get JSON data from the request
        request_data = request.get_json()

        # Extract data to insert from JSON data
        index = request_data.get("index")
        column_name = request_data.get("column_name")
        data_to_insert = request_data.get("data_to_insert")
        # Sample DataFrame for demonstration
        sample_data = {
            "A": [1, 2, 3], 
            "B": ["a", "b", "c"], 
            "C": [True, False, True]
        }
        df = pd.DataFrame(sample_data)
        # Insert data into DataFrame
        df.insert(index, column_name, data_to_insert)
        print(df)
        # Return updated DataFrame as JSON response
        return jsonify({"data_frame": df.to_dict()}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500


# make an api to insert a new data in data frame
@make_pandas_controller.route("/make-csv", methods=["Get"])
def make_csv_file():
    try:
        dis={"a":[1,2,3,4,5],"s":[1,2,3,4,5], "d": [1,2,3,4,5]}
        df=pd.DataFrame(dis)
        print(df)
        result = df.to_csv("dict_to_csv.csv", index=False)
        return jsonify({"data_frame": result}), 200
    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500
