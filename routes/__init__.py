# routes/__init__.py

from flask import Blueprint
from routes.auth_routes.auth_routes import auth_routes
from routes.numpy_routes.numpy_routes import numpy_routes

router = Blueprint('router', __name__)

router.register_blueprint(auth_routes, url_prefix='/api/v1/auth')
router.register_blueprint(numpy_routes, url_prefix='/api/v1/numpy')

