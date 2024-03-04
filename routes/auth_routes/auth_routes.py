# routes/auth_routes/auth_routes.py

from flask import Blueprint
from controllers.user_controllers.user_sign_up_controller import user_signup_controller
from controllers.user_controllers.user_login_controller import user_login_controller
from controllers.user_controllers.read_all_users_controller import read_all_users_controller
from controllers.user_controllers.get_user_by_id import get_user_by_id


auth_routes = Blueprint('auth_routes', __name__)

auth_routes.register_blueprint(user_signup_controller)
auth_routes.register_blueprint(user_login_controller)
# Register the route for reading all users
auth_routes.register_blueprint(read_all_users_controller)
# add a route and its dynamic route controller for fetch a single user record against its id
auth_routes.register_blueprint(get_user_by_id)