from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Maker(PermissionsMixin, AbstractBaseUser):

    identifier = models.CharField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)
    photo_url = models.URLField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    USERNAME_FIELD = 'identifier'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        return self.identifier

    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)
