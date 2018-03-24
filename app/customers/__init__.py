from flask import Blueprint

customers = Blueprint('customers', __name__)

from . import views
