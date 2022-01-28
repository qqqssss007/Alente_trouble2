from rest_framework import serializers


class AuthorizationSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True)