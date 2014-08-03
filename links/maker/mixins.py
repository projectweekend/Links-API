from rest_framework.permissions import AllowAny

from maker.models import Maker
from maker.serializers import (MakerSerializer,
                                MakerProfileSerializer,
                                ResetPasswordRequestSerializer,
                                ResetPasswordProcessSerializer)


class AuthenticatedMaker(object):

    serializer_class = MakerSerializer

    def get_queryset(self):
        return Maker.objects.get(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset()


class MakerProfile(object):

    serializer_class = MakerProfileSerializer


class ChangePassword(object):

    def change_password(self, new_password):
        user = self.get_object()
        user.set_password(new_password)
        user.save()


class PasswordReset(object):

    permission_classes = (AllowAny,)
    request_serializer = ResetPasswordRequestSerializer
    process_serializer = ResetPasswordProcessSerializer

    def find_user(self, email):
        try:
            return Maker.objects.get(email=email)
        except Maker.DoesNotExist:
            return None
