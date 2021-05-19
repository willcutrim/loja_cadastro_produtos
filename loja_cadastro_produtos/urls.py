from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_aplication.urls')),
    path('admin/', admin.site.urls),
]
