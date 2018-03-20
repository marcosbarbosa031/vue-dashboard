from flask import Blueprint

company = Blueprint('company', __name__)

from .model import Company
from . import views
