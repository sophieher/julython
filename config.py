import os

# configuration
DATABASE = 'postgres://postgres:sophie@localhost/food_mood'
DEBUG = True
SECRET_KEY = 'heyyy'
USERNAME = 'admin'
PASSWORD = ''
SQLALCHEMY_DATABASE_URI = DATABASE

UPLOAD_FOLDER = 'food_mood/static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
