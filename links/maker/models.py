import uuid
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from maker.managers import MakerManager, PasswordResetTokenManager


def password_reset_token():
    return str(uuid.uuid4())


class Maker(PermissionsMixin, AbstractBaseUser):

    REGULAR = 'RG'

    SIGNUP_TYPES = (
        (REGULAR, 'Regular'),
    )

    identifier = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)
    photo_url = models.URLField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    signup_type = models.CharField(max_length=2, choices=SIGNUP_TYPES,
                                    default=REGULAR)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MakerManager()

    def __unicode__(self):
        return self.identifier

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def change_email(self, new_email):
        self.email = new_email
        self.identifier = new_email
        self.save()


class PasswordResetToken(models.Model):

    maker = models.ForeignKey('Maker')
    token = models.CharField(max_length=50, default=password_reset_token)
    date = models.DateTimeField(auto_now_add=True)

    objects = PasswordResetTokenManager()

    def __unicode__(self):
        return "PW Reset Token: {0}".format(self.maker.identifier)

    @property
    def is_valid(self):
        self.date < datetime.now()
