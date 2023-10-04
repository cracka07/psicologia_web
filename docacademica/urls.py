from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_academica/', views.administracion_academica, name='administracion_academica'),
    path('other_academica/<str:subcarpeta_id>/', views.ver_other_academica, name='other_academica'),
    path('document/mostrar_archivos_academica/<str:subsubcarpeta_id>/', views.archivos_academica, name='mostrar_archivos_academica'),
   
]

