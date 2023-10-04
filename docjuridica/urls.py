from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_juridica/', views.administracion_juri, name='administracion_juridica'),
    path('other_juridica/<str:subcarpeta_id>/', views.ver_other_juri, name='other_juri'),
    path('document/mostrar_archivos_juridica/<str:subsubcarpeta_id>/', views.archivos_juri, name='mostrar_archivos_juri'),
   
]

