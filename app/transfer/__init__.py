from flask import Blueprint

transfer = Blueprint('transfer', __name__)

from .model import Transfer
from . import views
