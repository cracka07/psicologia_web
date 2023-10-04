from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_alumnos/', views.administracion_alumnos, name='administracion_alumnos'),
    path('other_alumnos/<str:subcarpeta_id>/', views.ver_other_alumnos, name='other_alumnos'),
    path('document/mostrar_archivos_alumnos/<str:subsubcarpeta_id>/', views.archivos_alumnos, name='mostrar_archivos_alumnos'),
   
]

