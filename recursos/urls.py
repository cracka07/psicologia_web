from django.urls import path
from . import views

urlpatterns = [
   
    
    path('documentos_administrativos/', views.administracion, name='administracion'),
   
]

