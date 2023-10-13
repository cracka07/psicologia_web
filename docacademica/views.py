from django.shortcuts import render
from recursos.views import obtener_access_token
from recursos.views import obtener_contenido_carpeta
from recursos.views import obtener_subcarpetas
import requests

def administracion_academica(request):
    access_token = request.access_token
    folder_id = "1v1Owd3Rp6JRtpAx0_9bpkn9pFiE0p1SV"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'academica/administracion_copy_academica.html', {'subcarpetas': subcarpetas})

def ver_other_academica(request, subcarpeta_id):
    access_token = request.access_token
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'academica/other_academica.html', {'subsubcarpetas': subsubcarpetas})

def archivos_academica(request,subsubcarpeta_id):
    access_token = request.access_token
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'academica/mostrar_archivos_academica.html', {'archivos': archivos})

