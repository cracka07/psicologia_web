from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_alumnos/', views.administracion_alumnos, name='administracion_alumnos'),
   
]

