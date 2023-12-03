from django.urls import path
from . import views

urlpatterns = [
    path('administrator/', views.admin, name='admin'),

    
    path('listar_archivos/', views.administracion, name='administracion'),
   
]

