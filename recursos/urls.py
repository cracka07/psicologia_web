from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos/', views.administracion, name='administracion'),
    path('other/<str:subcarpeta_id>/', views.ver_other, name='other'),
    path('document/mostrar_archivos/<str:subsubcarpeta_id>/', views.archivos, name='mostrar_archivos'),
]

