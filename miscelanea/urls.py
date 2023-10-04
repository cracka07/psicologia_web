from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_miscelanea/', views.administracion_miscelanea, name='administracion_miscelanea'),
    path('other_miscelanea/<str:subcarpeta_id>/', views.ver_other_miscelanea, name='other_miscelanea'),
    path('document/mostrar_archivos_miscelanea/<str:subsubcarpeta_id>/', views.archivos_miscelanea, name='mostrar_archivos_miscelanea'),
   
]

