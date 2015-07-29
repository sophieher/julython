from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message

from food_mood import app, mail


# TODO: write this
def send_email(recipient, subject, template):
    msg = Message(subject=subject, html=template ,sender="from@example.com", recipients=[recipient])
    mail.send(msg)

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])
