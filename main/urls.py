from django.urls import path
from . import views
from .views import autorTodos , autorId, autor_create, autor_delete, autor_update

urlpatterns = [
    path('autores', views.autorTodos, name='autores'),
    path('autorId/<int:id>', views.autorId, name='autorId'),
    path('autor/create/', views.autor_create, name='autor-create'),
    path('autor/<int:id>/update/', views.autor_update, name='autor-update'),
    path('autor/<int:id>/delete/', views.autor_delete, name='autor-delete'),
]
