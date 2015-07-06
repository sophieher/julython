# all the imports
from flask import Flask
app = Flask(__name__)
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

engine = create_engine(DATABASE, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from food_mood import models, views
