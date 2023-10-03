from django.urls import path
from . import views
from .views import autorTodos, autor_create, autor_delete, autor_update

urlpatterns = [
    path('autores', views.autorTodos, name='autores'),
    path('autor/create/', views.autor_create, name='autor-create'),
    path('autor/<int:id>/update/', views.autor_update, name='autor-update'),
    path('autor/<int:id>/delete/', views.autor_delete, name='autor-delete'),
]
