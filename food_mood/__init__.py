# all the imports
from flask import Flask
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# configuration
DATABASE = 'postgres://postgres:sophie@localhost/food_mood'
DEBUG = True
SECRET_KEY = 'heyyy'
USERNAME = 'admin'
PASSWORD = ''


app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from food_mood import models, views
