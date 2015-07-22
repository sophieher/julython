from itsdangerous import URLSafeTimedSerializer
from flask.ext.mail import Mail, Message

from food_mood import app

mail = Mail()
mail.init_app(app)


# TODO: write this
def send_email(recipient, subject, template):
    pass

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
