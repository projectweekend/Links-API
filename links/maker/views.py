from django.db import IntegrityError
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from maker.models import (Maker,
                            PasswordResetToken,
                            EmailChangeToken,
                            EmailVerificationToken)
from maker.serializers import (RegistrationRequestSerializer,
                                AuthenticationRequestSerializer,
                                AuthenticationResponseSerializer,
                                ChangePasswordSerializer,
                                EmailChangeRequestSerializer,
                                EmailChangeProcessSerializer)
from maker.mixins import (AuthenticatedMaker,
                            MakerProfile,
                            ChangePassword,
                            PasswordReset)


class RegsitrationView(generics.GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegistrationRequestSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            email = serializer.data['email'].lower()

            user = Maker.objects.create_user(
                identifier=email,
                password=serializer.data['password'],
                first_name = serializer.data['first_name'],
                last_name = serializer.data['last_name'],
                email = email)
        except IntegrityError:
            content = {'message': 'This email is in use'}
            return Response(content, status=status.HTTP_409_CONFLICT)

        EmailVerificationToken(maker=user)
        auth_token = Token.objects.create(user=user)

        response = AuthenticationResponseSerializer()
        response.data['token'] = auth_token.key

        return Response(response.data, status=status.HTTP_201_CREATED)


class AuthenticationView(generics.GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = AuthenticationRequestSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['identifier'],
                            password=serializer.data['password'])

        if user is not None:
            token = Token.objects.get(user__pk=user.pk)

            response = AuthenticationResponseSerializer()
            response.data['token'] = token.key

            return Response(response.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ResetPasswordRequestView(PasswordReset, generics.GenericAPIView):

    def post(self, request):
        serializer = self.request_serializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = self.find_user(request.DATA['email'])
        if user:
            PasswordResetToken.objects.create_and_send(user)

        return Response(status=status.HTTP_201_CREATED)


class ResetPasswordProcessView(PasswordReset, generics.GenericAPIView):

    def post(self, request):
        serializer = self.process_serializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            reset_request = PasswordResetToken.objects.get(token=request.DATA['token'])
        except PasswordResetToken.DoesNotExist:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        if not reset_request.is_valid:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        reset_request.maker.set_password(request.DATA['new_password'])
        reset_request.maker.save()
        return Response(status=status.HTTP_200_OK)


class EmailChangeRequestView(AuthenticatedMaker, generics.GenericAPIView):

    def post(self, request):
        if self.request.user.signup_type != 'RG':
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = EmailChangeRequestSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        new_email = request.DATA['new_email']

        try:
            Maker.objects.get(email=new_email)
        except Maker.DoesNotExist:
            EmailChangeToken.objects.create_and_send(self.request.user, new_email)
            return Response(status=status.HTTP_201_CREATED)
        else:
            content = {'message': 'This email is in use'}
            return Response(content, status=status.HTTP_409_CONFLICT)


class EmailChangeProcessView(AuthenticatedMaker, generics.GenericAPIView):

    def post(self, request):
        if self.request.user.signup_type != 'RG':
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = EmailChangeProcessSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            change_request = EmailChangeToken.objects.get(token=request.DATA['token'])
        except EmailChangeToken.DoesNotExist:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        if not change_request.is_valid:
            return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        self.request.user.change_email(change_request.new_email)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(AuthenticatedMaker, ChangePassword, generics.GenericAPIView):

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.change_password(request.DATA['new_password'])
        return Response(status=status.HTTP_201_CREATED)


class MakerSelfView(AuthenticatedMaker, generics.RetrieveUpdateAPIView):
    pass


class MakerProfileListView(MakerProfile, generics.ListAPIView):
    pass


class MakerProfileDetailView(MakerProfile, generics.RetrieveAPIView):
    pass
