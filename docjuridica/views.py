from django.shortcuts import render
from recursos.views import obtener_access_token, obtener_o_renovar_access_token, obtener_contenido_carpeta, obtener_subcarpetas
import requests



def administracion_juri(request):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1rBxdmL9JDgKqprer16CPoug4Lbl-WJrg"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'juridica/administracion_copy_juridica.html', {'subcarpetas': subcarpetas})

def ver_other_juri(request, subcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'juridica/other_juridica.html', {'subsubcarpetas': subsubcarpetas})

def archivos_juri(request,subsubcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'juridica/mostrar_archivos_juridica.html', {'archivos': archivos})

