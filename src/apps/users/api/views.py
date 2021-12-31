from django.contrib.auth import get_user_model

from .serializers import (
    MemberDetailSerializer,
    MemberListSerializer,
    MemberRagisterSerializer)

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


Member = get_user_model()


class MemberListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemberListSerializer
    queryset = Member.objects.all()


class MemberCreateApiView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MemberRagisterSerializer
    queryset = Member.objects.all()


class MemberDetailApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = MemberDetailSerializer(request.user)
        return Response(serializer.data)
