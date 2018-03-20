from flask import Blueprint

boleto = Blueprint('boleto', __name__)

from .model import Boleto
from . import views
