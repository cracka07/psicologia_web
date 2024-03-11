from django.urls import path
from . import views

urlpatterns = [
    path('', views.doc_psico, name='doc_psico'),
    path('unc/', views.unc, name='doc_unc'),
    path('unc_publicaciones/', views.unc_publish, name='unc_publish'),
    path('unc_ffyh/', views.unc_ffyh, name='unc_ffyh'),

 
]
