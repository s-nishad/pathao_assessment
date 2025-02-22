from rest_framework import serializers
from .models import User, UserTag


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'password', 'phone']


class UserDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone']

    def get_name(self, obj):
        return f"{obj.firstName} {obj.lastName}"


class UserTagSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=50))
    expiry = serializers.IntegerField()

    class Meta:
        model = UserTag
        fields = ['tags', 'expiry']


class UserQuerySerializer(serializers.Serializer):
    tags = serializers.CharField(help_text="Comma-separated list of tags", required=True)
