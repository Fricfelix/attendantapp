from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates',url_prifix="/auth")

from . import routes