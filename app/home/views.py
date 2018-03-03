from flask import render_template, jsonify, request, abort
from werkzeug.security import generate_password_hash
from app import app
import requests


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template('index.html')
