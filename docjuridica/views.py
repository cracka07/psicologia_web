from django.shortcuts import render
from recursos.views import obtener_access_token
from recursos.views import obtener_contenido_carpeta
from recursos.views import obtener_subcarpetas
import requests

def administracion_juri(request):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"
    access_token = obtener_access_token(refresh_token)
    folder_id = "14kH1lYFp7geQwVK5WOj1labymNUyL2vL"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'juridica/administracion_copy_juridica.html', {'subcarpetas': subcarpetas})

def ver_other_juri(request, subcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'juridica/mostrar_archivos_juridica.html', {'subsubcarpetas': subsubcarpetas})

def archivos_juri(request,subsubcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'juridica/mostrar_archivos_juridica.html', {'archivos': archivos})

