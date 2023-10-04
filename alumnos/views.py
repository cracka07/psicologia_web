from django.shortcuts import render
from recursos.views import obtener_access_token
from recursos.views import obtener_contenido_carpeta
from recursos.views import obtener_subcarpetas
import requests

def administracion_alumnos(request):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"
    access_token = obtener_access_token(refresh_token)
    folder_id = "1HAmIyoF1mA6-xkqOm6wgITtKr0t8Yr4F"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'alumnos/administracion_copy_alumnos.html', {'subcarpetas': subcarpetas})

def ver_other_alumnos(request, subcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'alumnos/other_alumnos.html', {'subsubcarpetas': subsubcarpetas})

def archivos_alumnos(request,subsubcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'alumnos/mostrar_archivos_alumnos.html', {'archivos': archivos})

