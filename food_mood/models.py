from datetime import datetime
from flask import current_app as app

from food_mood import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.Integer, default=1)   # number of the meal, 1 for breakfast, etc
    food = db.Column(db.String(200))
    mood = db.Column(db.Integer, default=5)  # mood from 1 sucky to 10 the best
    pub_date = db.Column(db.Date(), default=datetime.today, nullable=False)
    eater = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return self.food


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    _password = db.Column('password', db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    entries = db.relationship('Entry', backref='user', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    @property
    def password(self):
        return self._password

    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return self.username


# class UserProfile(db.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='profile')

#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     photo = models.ImageField(upload_to='/static/profile_images/', blank=True)

#     # thanks to sarahhagstrom for this unicode output
#     def __unicode__(self):
#         return "{}'s profile".format(self.user.username)

#     def profile_image_url(self):
#         uid = SocialAccount.objects.filter(user_id=self.user.id)

#         if len(uid):
#             return uid[0].get_avatar_url()

#         return self.photo.url[47:]

#         class Meta:
#             db_table = 'user_profile'

#             def account_verified(self):
#                 if self.user.is_authenticated:
#                     result = EmailAddress.objects.filter(email=self.user.email)
#                     if len(result):
#                         return result[0].verified
#                         return False

#                         User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
