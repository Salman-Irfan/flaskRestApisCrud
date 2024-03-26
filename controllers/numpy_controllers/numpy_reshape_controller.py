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
