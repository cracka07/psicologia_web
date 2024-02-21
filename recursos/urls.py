from django.urls import path
from . import views

urlpatterns = [
    path('administrator/', views.admin, name='admin'),
    # path('gallery/', views.galeria, name='galeria'),

    
    path('listar_archivos/', views.administracion, name='administracion'),
   
]

