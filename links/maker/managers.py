from django.contrib.auth.models import BaseUserManager


class MakerManager(BaseUserManager):

    def create_user(self, identifier, password, first_name,
                    last_name, bio="", photo_url=""):

        user = self.model(identifier=identifier,
                            first_name=first_name,
                            last_name=last_name,
                            bio=bio,
                            photo_url=photo_url)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, identifier, password):

        user = self.create_user(identifier=identifier,
                                first_name="Super",
                                last_name="User")

        user.is_superuser = True
        user.is_admin = True
        user.save()

        return user

