# routes/numpy_routes/numpy_routes.py

from flask import Blueprint
from controllers.numpy_controllers.read_numpy_controller import (
    read_numpy_controller,
)
from controllers.numpy_controllers.arithmetic_controller import (
    arithmetic_controller,
)
from controllers.numpy_controllers.numpy_functions_controller import (
    numpy_functions_controller,
)

numpy_routes = Blueprint("numpy_routes", __name__)

numpy_routes.register_blueprint(read_numpy_controller)
numpy_routes.register_blueprint(arithmetic_controller)
numpy_routes.register_blueprint(numpy_functions_controller)
