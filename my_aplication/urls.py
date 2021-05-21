from django.urls.conf import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.cadastrar_produtos, name='home'),
    path('deletar/<int:id>/', views.deletar_produto, name='deletar'),
    path('<int:id>/', views.editar_produto, name='editar'),
]