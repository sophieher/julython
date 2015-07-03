# all the imports
from flask import Flask, render_template

# configuration
DATABASE = ''
DEBUG = True
SECRET_KEY = 'heyyy'
USERNAME = 'admin'
PASSWORD = ''

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
