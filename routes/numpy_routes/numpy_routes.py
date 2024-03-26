# routes/numpy_routes/numpy_routes.py

from flask import Blueprint
from controllers.numpy_controllers.read_numpy_controller import (
    read_numpy_controller,
)

numpy_routes = Blueprint("numpy_routes", __name__)

numpy_routes.register_blueprint(read_numpy_controller)
