from flask import Blueprint

deposit = Blueprint('deposit', __name__)

from .model import Deposit
from . import views
