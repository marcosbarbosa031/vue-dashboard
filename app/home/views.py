from flask import render_template
from . import home


@home.route('/', defaults={'path': ''})
@home.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')
