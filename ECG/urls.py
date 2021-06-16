from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('patient.urls')),
    path('', include('pwa.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
