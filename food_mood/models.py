from datetime import datetime

from food_mood import db


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.Integer, default=1)   # number of the meal, 1 for first, etc
    food = db.Column(db.String(200))
    mood = db.Column(db.Integer, default=5)  # mood from 1 sucky to 10 the best
    pub_date = db.Column(db.Date(), default=datetime.today, nullable=False)
    # eater = db.Column(ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='entries'))

    def __repr__(self):
        return self.food


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
