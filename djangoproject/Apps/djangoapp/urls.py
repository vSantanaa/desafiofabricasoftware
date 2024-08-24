from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),  # Ver todos os usuarios
    path('create', views.addUser),  # Criar usuario
    path('read/<int:pk>', views.getUser),  # Ver usuario especifico
    path('update/<int:pk>', views.updateUser),  # Atualizar Usuario
    path('delete/<int:pk>', views.deleteUser),  # Excluir usuario
]
