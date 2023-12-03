from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_academica/', views.administracion_academica, name='administracion_academica'),
   
]

