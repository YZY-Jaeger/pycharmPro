from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/sdw?charset=utf8'
db = SQLAlchemy(app)

class heroku_46565dbb12b46e3(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
