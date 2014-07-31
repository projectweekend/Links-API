from django.db import IntegrityError

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from maker.models import Maker
from maker.serializers import (RegistrationRequestSerializer,
    RegistrationResponseSerializer)


class RegsitrationView(generics.GenericAPIView):

    def post(self, request):
        serializer = RegistrationRequestSerializer(data=request.data)

        if serializer.is_valid():
            try:
                user = Maker.objects.create_user(
                    identifier=serializer.data['identifier'],
                    password=serializer.data['password'],
                    first_name = serializer.data['first_name'],
                    last_name = serializer.data['last_name'],
                    email = serializer.data['email'])
            except IntegrityError:
                content = {'message': 'This user is taken'}
                return Response(content, status=status.HTTP_409_CONFLICT)

            token = Token.objects.create(user=user)

            response_data = {
                'id': user.pk,
                'token': token.key
            }
            response = RegistrationResponseSerializer(data=response_data)

            return Response(response.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
