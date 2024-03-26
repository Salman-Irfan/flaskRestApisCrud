from flask import Blueprint, jsonify, request
import numpy as np

arithmetic_controller = Blueprint("arithmetic_controller", __name__)


@arithmetic_controller.route("/add", methods=["POST"])
def add_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.add(array1,array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/sub", methods=["POST"])
def subtract_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.subtract(array1, array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/mul", methods=["POST"])
def multiply_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.multiply(array1, array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/div", methods=["POST"])
def divide_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.divide(array1, array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/mod", methods=["POST"])
def modulus_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.mod(array1, array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/power", methods=["POST"])
def power_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        array2 = np.array(data["array2"])
        result = np.power(array1, array2)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@arithmetic_controller.route("/reciprocal", methods=["POST"])
def reciprocal_array():
    try:
        data = request.get_json()
        array1 = np.array(data["array1"])
        result = np.reciprocal(array1)
        return jsonify({"result": result.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
