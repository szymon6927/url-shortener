from flask import Blueprint

opened = Blueprint('opened', __name__)

from . import views