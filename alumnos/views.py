from django.shortcuts import render
from recursos.views import obtener_access_token, obtener_contenido_carpeta, obtener_subcarpetas
import requests





def administracion_alumnos(request):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"
    access_token = obtener_access_token(refresh_token)
    folder_id = "1HAmIyoF1mA6-xkqOm6wgITtKr0t8Yr4F"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'alumnos/administracion_copy_alumnos.html', {'subcarpetas': subcarpetas})

def ver_other_alumnos(request, subcarpeta_id):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"

    access_token = obtener_access_token(refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'alumnos/other_alumnos.html', {'subsubcarpetas': subsubcarpetas})

def archivos_alumnos(request,subsubcarpeta_id):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"

    access_token = obtener_access_token(refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'alumnos/mostrar_archivos_alumnos.html', {'archivos': archivos})

