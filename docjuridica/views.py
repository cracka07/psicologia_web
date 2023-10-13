from django.shortcuts import render
from recursos.views import obtener_access_token, obtener_contenido_carpeta

from recursos.views import obtener_subcarpetas
import requests



def administracion_juri(request):
    access_token = request.access_token
    folder_id = "1rBxdmL9JDgKqprer16CPoug4Lbl-WJrg"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'juridica/administracion_copy_juridica.html', {'subcarpetas': subcarpetas})

def ver_other_juri(request, subcarpeta_id):
    access_token = request.access_token
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'juridica/other_juridica.html', {'subsubcarpetas': subsubcarpetas})

def archivos_juri(request,subsubcarpeta_id):
    access_token = request.access_token
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'juridica/mostrar_archivos_juridica.html', {'archivos': archivos})

