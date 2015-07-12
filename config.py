# configuration
DATABASE = 'postgres://postgres:sophie@localhost/food_mood'
DEBUG = True
SECRET_KEY = 'heyyy'
USERNAME = 'admin'
PASSWORD = ''
SQLALCHEMY_DATABASE_URI = DATABASE

UPLOAD_FOLDER = 'food_mood/static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
