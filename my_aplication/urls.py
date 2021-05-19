from django.urls.conf import path
from django.urls import path
from my_aplication import views

urlpatterns = [
    path('', views.index, name='index'),
]