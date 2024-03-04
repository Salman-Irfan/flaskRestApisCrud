# routes/auth_routes/auth_routes.py

from flask import Blueprint
from controllers.user_controllers.user_sign_up_controller import user_signup_controller
from controllers.user_controllers.user_login_controller import user_login_controller

auth_routes = Blueprint('auth_routes', __name__)

auth_routes.register_blueprint(user_signup_controller)
auth_routes.register_blueprint(user_login_controller)
