from wtforms import Form, BooleanField, IntegerField, TextField, PasswordField, validators
from flask.ext.wtf.html5 import NumberInput


class SignupForm(Form):
    username = TextField('username', [validators.Length(min=3, max=64)])
    email = TextField('email', [validators.Length(min=6, max=120)])
    password = PasswordField('password', [validators.Length(min=8), validators.Required()])


class LoginForm(Form):
    username = TextField('username', [validators.Length(min=3, max=64)])
    password = PasswordField('password', [validators.Length(min=8), validators.Required()])


class AddForm(Form):
    meal = IntegerField(widget=NumberInput())
    food = TextField()
    mood = IntegerField(widget=NumberInput())
