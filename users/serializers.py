from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.save()

        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        elif self.instance and self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data