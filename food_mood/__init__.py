# all the imports

from flask import Flask
app = Flask(__name__)

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_mail import Mail
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

engine = create_engine(app.config['DATABASE'], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

from food_mood import models, views
