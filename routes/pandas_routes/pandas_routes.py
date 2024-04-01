from flask import Blueprint
from controllers.pandas_controllers.make_pandas_controller import (
    make_pandas_controller,
)

pandas_routes = Blueprint("pandas_routes", __name__)

pandas_routes.register_blueprint(make_pandas_controller)
