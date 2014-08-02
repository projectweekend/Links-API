from django.db import IntegrityError
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from maker.models import Maker
from maker.serializers import (RegistrationRequestSerializer,
                                AuthenticationRequestSerializer,
                                AuthenticationResponseSerializer,
                                ChangePasswordSerializer)
from maker.mixins import AuthenticatedMaker, ChangePassword


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

        token = Token.objects.create(user=user)

        response = AuthenticationResponseSerializer()
        response.data['token'] = token.key

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


class ChangePasswordView(AuthenticatedMaker, ChangePassword, generics.GenericAPIView):

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.change_password(request.DATA['new_password'])
        return Response(status=status.HTTP_201_CREATED)


class MakerSelfView(AuthenticatedMaker, generics.RetrieveUpdateAPIView):

    pass
