from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from apps.users.models import Member


# Member = get_user_model()


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username',
                  'first_name', 'last_name',
                  'email', 'password',
                  'sex', 'profile_photo',)

    # def validate_password(self, value: str) -> str:
    #     return make_password(value)

    def create(self, validated_data):
        return Member.objects.create_user(**validated_data)
