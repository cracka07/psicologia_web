from django.shortcuts import render
from recursos.views import   obtener_contenido_carpeta, obtener_o_renovar_access_token, obtener_subcarpetas
import requests





def administracion_alumnos(request):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1HAmIyoF1mA6-xkqOm6wgITtKr0t8Yr4F"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'alumnos/administracion_copy_alumnos.html', {'subcarpetas': subcarpetas})

def ver_other_alumnos(request, subcarpeta_id):
    refresh_token="1//0h3pQxZ468uI7CgYIARAAGBESNwF-L9IrwPUfoModZ4tk2NxbdJl_219ZOYg_FwLeLBuxpzVwbLtTlESTwRTALODr5aoyKn1OX8I"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'alumnos/other_alumnos.html', {'subsubcarpetas': subsubcarpetas})

def archivos_alumnos(request,subsubcarpeta_id):
    refresh_token="1//0h3pQxZ468uI7CgYIARAAGBESNwF-L9IrwPUfoModZ4tk2NxbdJl_219ZOYg_FwLeLBuxpzVwbLtTlESTwRTALODr5aoyKn1OX8I"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'alumnos/mostrar_archivos_alumnos.html', {'archivos': archivos})

