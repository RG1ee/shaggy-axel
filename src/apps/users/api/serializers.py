from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from apps.users.models import Member


# Member = get_user_model()


class MemberRagisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username', 'password',
                  'first_name', 'last_name',
                  'sex', 'profile_photo')

    def create(self, validated_data):
        return Member.objects.create_user(**validated_data)

class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('username', 'first_name', 'last_name')
