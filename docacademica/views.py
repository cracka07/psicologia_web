from django.shortcuts import render
from recursos.views import obtener_access_token, obtener_o_renovar_access_token, obtener_contenido_carpeta, obtener_subcarpetas
import requests



def administracion_academica(request):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1v1Owd3Rp6JRtpAx0_9bpkn9pFiE0p1SV"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'academica/administracion_copy_academica.html', {'subcarpetas': subcarpetas})

def ver_other_academica(request, subcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'academica/other_academica.html', {'subsubcarpetas': subsubcarpetas})

def archivos_academica(request,subsubcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'academica/mostrar_archivos_academica.html', {'archivos': archivos})

