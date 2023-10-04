from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_invest/', views.administracion_invest, name='administracion_investigacion'),
    path('other_invest/<str:subcarpeta_id>/', views.ver_other_invest, name='other_investigacion'),
    path('document/mostrar_archivos_investigacion/<str:subsubcarpeta_id>/', views.archivos_invest, name='mostrar_archivos_investigacion'),
   
]

