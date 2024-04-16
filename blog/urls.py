from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post/<int:pk>/ el URL comienza como post y toma la llave primaria de la publicacion escogida
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]