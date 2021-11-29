from django.contrib.auth import get_user_model

from .serializers import MemberSerializer
from rest_framework import viewsets, generics, status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


Member = get_user_model()


class MemberListApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class MemberCreateApiView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class MemberDetailApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer