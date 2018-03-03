from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<>\nid: {}\nusername: {}\nemail: {}\n<>".format(self.id, self.username, self.email)


# admin = User('admin', 'admin@example.com', '123153464')

users = Users.query.filter_by(username='marcos31').first()

print (users)

