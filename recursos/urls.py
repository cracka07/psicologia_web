from django.urls import path
from . import views

urlpatterns = [
   
    
 path('administrator/', views.admin, name='admin'),
 path('doc_alumnos/', views.doc_alumnos, name='doc_alumnos'),
 path('doc_docentes/', views.doc_docentes, name='doc_docentes'),
 path('doc_compras/', views.doc_compras, name='doc_compras'),

    
   
]

