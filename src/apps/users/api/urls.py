from . import views
from django.urls import path, include
# from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'', views.MemberViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.MemberListApiView.as_view(), name='users'),
    path('<int:pk>/', views.MemberDetailApiView.as_view(), name='user'),
    path('create/', views.MemberCreateApiView.as_view(),
         name='users-register'),
]