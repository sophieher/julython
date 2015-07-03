# all the imports
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import models

# configuration
DATABASE = ''
DEBUG = True
SECRET_KEY = 'heyyy'
USERNAME = 'admin'
PASSWORD = ''

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:sophie@localhost/food_mood'
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
