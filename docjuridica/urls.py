from django.urls import path
from . import views

urlpatterns = [
    path('listar_archivos_juridica/', views.administracion_juri, name='administracion_juridica'),

]

