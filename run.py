import requests
from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from backend.config import Config
from backend/auth.user import Users

app = Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

# db = pymysql.connect(Config.db_host, Config.db_username, Config.db_password, Config.db_name, cursorclass=pymysql.cursors.DictCursor)


# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults = {'path' : ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template('index.html')

@app.route('/user/login', methods = ['POST'])
def login_user():
    try:
        if not request.json:
            return abort(500)
        username = request.json.get('user')
        password = request.json.get('pass')

        with db.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (username))
            result = cursor.fetchone()
            if not result:
                return "Invalid Username"
            else:
                if result['password'] == password:
        
    finally:
        pass


    response = {
        'login' : True
    }
    return jsonify(response)

@app.route('/api/banco')
def connection():
    try:
        with db.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            results = cursor.fetchone()
    finally:
        db.close()


    return str(results)
    # return render_template('index.html', results = results)
