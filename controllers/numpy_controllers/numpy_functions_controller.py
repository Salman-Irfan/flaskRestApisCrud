from flask import Blueprint, jsonify, request
import numpy as np

numpy_functions_controller = Blueprint("numpy_functions_controller", __name__)


@numpy_functions_controller.route("/min", methods=["POST"])
def min_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.min(array)
        return jsonify({"result": int(result)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/max", methods=["POST"])
def max_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.max(array)
        return jsonify({"result": int(result)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/argmin", methods=["POST"])
def argmin_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.argmin(array)
        return jsonify({"result": int(result)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/sqrt", methods=["POST"])
def sqrt_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.sqrt(array)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/sin", methods=["POST"])
def sin_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.sin(array)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/cos", methods=["POST"])
def cos_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.cos(array)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@numpy_functions_controller.route("/cumsum", methods=["POST"])
def cumsum_array():
    try:
        data = request.get_json()
        array = np.array(data["array"])
        result = np.cumsum(array)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
