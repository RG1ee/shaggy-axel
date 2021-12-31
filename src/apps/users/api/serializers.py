from rest_framework import serializers
from apps.users.models import Member


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
