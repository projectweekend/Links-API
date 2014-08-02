from maker.models import Maker
from maker.serializers import MakerSerializer, ResetPasswordRequestSerializer


class AuthenticatedMaker(object):

    serializer_class = MakerSerializer

    def get_queryset(self):
        return Maker.objects.get(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset()


class ChangePassword(object):

    def change_password(self, new_password):
        user = self.get_object()
        user.set_password(new_password)
        user.save()


class PasswordResetRequest(object):

    serializer_class = ResetPasswordRequestSerializer

    def find_user(self, email):
        try:
            return Maker.objects.get(email=email)
        except Maker.DoesNotExist:
            return None
