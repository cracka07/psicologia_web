from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_miscelanea/', views.administracion_miscelanea, name='administracion_miscelanea'),
  
]


