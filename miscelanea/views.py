from django.shortcuts import render
from recursos.views import obtener_access_token
from recursos.views import obtener_contenido_carpeta
from recursos.views import obtener_subcarpetas
import requests

def administracion_miscelanea(request):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"
    access_token = obtener_access_token(refresh_token)
    folder_id = "1JuZdzpu84Uh1pIsxvUqa8Q4hyGahr1gt"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'miscelanea/administracion_copy_miscelanea.html', {'subcarpetas': subcarpetas})

def ver_other_miscelanea(request, subcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'miscelanea/other_miscelanea.html', {'subsubcarpetas': subsubcarpetas})

def archivos_miscelanea(request,subsubcarpeta_id):
    refresh_token="1//0hGiBm8aolYjzCgYIARAAGBESNwF-L9IrxbYgM_DMukowxb4vLWzHj4vhHdNPYXMuJXxZtj73eSfUNJD7SDVzXNR3b71-YmRsBoE"

    access_token = obtener_access_token(refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'miscelanea/mostrar_archivos_miscelanea.html', {'archivos': archivos})

