from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates',url_prifix="/users")

from . import routes