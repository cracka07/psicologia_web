from django.shortcuts import render
from recursos.views import obtener_access_token
from recursos.views import obtener_contenido_carpeta
from recursos.views import obtener_subcarpetas
import requests

def administracion_miscelanea(request):
    access_token = request.access_token
    folder_id = "1JuZdzpu84Uh1pIsxvUqa8Q4hyGahr1gt"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'miscelanea/administracion_copy_miscelanea.html', {'subcarpetas': subcarpetas})

def ver_other_miscelanea(request, subcarpeta_id):
    access_token = request.access_token
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'miscelanea/other_miscelanea.html', {'subsubcarpetas': subsubcarpetas})

def archivos_miscelanea(request,subsubcarpeta_id):
    access_token = request.access_token
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'miscelanea/mostrar_archivos_miscelanea.html', {'archivos': archivos})

