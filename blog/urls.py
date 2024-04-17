from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post/<int:pk>/ el URL comienza como post y toma la llave primaria de la publicacion escogida
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post/new es URL para crear una nueva publicacion
    path('post/new', views.post_new, name='post_new'),
    #post/pk del post/edit para identificar el post a editar
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]