from flask import Blueprint, jsonify, request
import numpy as np

numpy_reshape_controller = Blueprint("numpy_reshape_controller", __name__)


@numpy_reshape_controller.route("/shape", methods=["POST"])
def get_shape():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        shape = array.shape
        return jsonify({"shape": shape}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_reshape_controller.route("/reshape", methods=["POST"])
def reshape_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        new_shape = tuple(data["new_shape"])
        reshaped_array = np.reshape(array, new_shape)
        return jsonify({"reshaped_array": reshaped_array.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# make a controller for ndenumerate to iterate a three dimensional array
@numpy_reshape_controller.route("/ndenumerate", methods=["POST"])
def ndenumerate_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])

        # Initialize a list to store enumerated elements
        enumerated_elements = []

        # Iterate through the array using ndenumerate
        for index, value in np.ndenumerate(array):
            # Convert value to int for JSON serialization
            value = int(value)
            enumerated_elements.append({"index": index, "value": value})

        return jsonify({"enumerated_elements": enumerated_elements}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# make controllers for joining and split (concatenate, stack & array split)
@numpy_reshape_controller.route("/concatenate", methods=["POST"])
def concatenate_arrays():
    try:
        data = request.get_json()
        arrays = [np.array(arr) for arr in data["arrays"]]
        axis = data.get("axis", 0)
        result = np.concatenate(arrays, axis=axis)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# stack
@numpy_reshape_controller.route("/stack", methods=["POST"])
def stack_arrays():
    try:
        data = request.get_json()
        arrays = [np.array(arr) for arr in data["arrays"]]
        axis = data.get("axis", 0)
        result = np.stack(arrays, axis=axis)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# array-split
@numpy_reshape_controller.route("/array-split", methods=["POST"])
def array_split():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        sections = data.get("sections", 2)
        result = np.array_split(array, sections)
        return jsonify({"result": [arr.tolist() for arr in result]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
