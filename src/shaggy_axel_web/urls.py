from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.main.views import render_main
from apps.resume.views import resume_view
from apps.timetable.views import timetable_render_view


urlpatterns = [
    path('', render_main),
    path('admin/', admin.site.urls),
    path("api/auth/", include(
        "rest_framework.urls",
        namespace="rest_framework")),
    path('api/users/', include('apps.users.api.urls')),
    path('resume/', resume_view, name="shaggy-resume"),
    path('blog/', include('apps.blog.urls')),
    path('timetable/', timetable_render_view)
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
