from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Maker(AbstractBaseUser, PermissionsMixin):

    identifier = models.CharField(max_length=200, unique=True)
    is_admin = models.BooleanField(default=False)
    photo_url = models.URLField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    USERNAME_FIELD = 'identifier'
