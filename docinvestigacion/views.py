from django.shortcuts import render
from recursos.views import obtener_access_token, obtener_o_renovar_access_token, obtener_contenido_carpeta, obtener_subcarpetas
import requests



def administracion_invest(request):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1axJ3Yb0BrgJ7YKCp34K8peSE_HuV_6AE"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'invest/administracion_copy_invest.html', {'subcarpetas': subcarpetas})

def ver_other_invest(request, subcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)

    # Obtener los archivos .jpg de la subcarpeta
    archivos_jpg = [archivo for archivo in subsubcarpetas if archivo['name'].lower().endswith('.jpg')]

    return render(request, 'invest/other_invest.html', {'subsubcarpetas': subsubcarpetas, 'archivos_jpg': archivos_jpg})


def archivos_invest(request,subsubcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'invest/mostrar_archivos_invest.html', {'archivos': archivos})

