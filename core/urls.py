from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings.yasg import urlpatterns_swagger as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/chair/', include('apps.chairs.urls')),
    path('api/v1/users/', include('apps.users.urls')),
] + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
