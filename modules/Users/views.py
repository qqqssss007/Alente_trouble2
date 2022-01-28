import blank as blank
from django.contrib.auth.hashers import make_password, check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import modules.Users.models
from modules.Users.serializers.autorization import AuthorizationSerializer
from modules.Users.serializers.registration import RegistrationSerializer
from modules.Users.models import User


@swagger_auto_schema(method='post', request_body=RegistrationSerializer)
@api_view(['POST'])
@permission_classes((AllowAny,))
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = User.objects.create(**serializer.data,
                                   password=make_password(12345678),
                                   username=request.data['email'])




@swagger_auto_schema(method='post', request_body=AuthorizationSerializer)
@api_view(['POST'])
@permission_classes((AllowAny,))
def authorization(request):
    serializer = AuthorizationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        username = request.data['email']
        user_password = request.data['password']
        user = User.objects.get(username=username)
        token = Token.objects.get(user=user.id)
        if check_password(user_password, user.password):
            return Response({'token': token.key})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Некорректный пароль')
