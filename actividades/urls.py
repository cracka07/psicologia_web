from django.urls import path
from . import views

urlpatterns = [
    path('', views.activity, name='activities'),
    # path('upload/', views.upload_file, name='upload_image'),
    # path('eliminar-imagen/', views.eliminar_imagen, name='eliminar_imagen'),

]