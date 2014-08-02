from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager


class MakerManager(BaseUserManager):

    def create_user(self, identifier, password=None, first_name=None,
                    last_name=None, email=None, bio="", photo_url=""):

        user = self.model(identifier=identifier,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            bio=bio,
                            photo_url=photo_url)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, identifier, password, email):

        user = self.create_user(identifier=identifier,
                                password=password,
                                first_name="Super",
                                last_name="User",
                                email=email)

        user.is_superuser = True
        user.is_admin = True
        user.save()

        return user


class PasswordResetTokenManager(Manager):

    def create_and_send(self, user):
        token = self.model(maker=user)
        token.save()
        #TODO: pass message to email queue here
