from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_invest/', views.administracion_invest, name='administracion_investigacion'),
   
]

