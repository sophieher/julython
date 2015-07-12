from flask.ext.wtf import Form
from wtforms import FileField, IntegerField, TextField, PasswordField, validators


class SignupForm(Form):
    username = TextField('username', [validators.Length(min=3, max=64)])
    email = TextField('email', [validators.Length(min=6, max=120)])
    password = PasswordField('password', [validators.Length(min=8), validators.Required()])


class LoginForm(Form):
    username = TextField('username', [validators.Length(min=3, max=64)])
    password = PasswordField('password', [validators.Length(min=8), validators.Required()])


class AddForm(Form):
    meal = IntegerField()
    food = TextField()
    mood = IntegerField()


class PhotoForm(Form):
    image = FileField('Image File')
