from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.MemberListApiView.as_view(), name='users'),
    path('profile/', views.MemberDetailApiView.as_view(), name='user'),
    path('register/', views.MemberCreateApiView.as_view(),
         name='users-register'),
]
