from flask import Blueprint

card = Blueprint ('card', __name__)

from .model import Card
from . import views