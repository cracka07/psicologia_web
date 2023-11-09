import time
from django.http import HttpResponse
from django.shortcuts import render
import requests



def obtener_o_renovar_access_token(request, refresh_token):
    access_token = request.session.get('access_token')
    expires_at = request.session.get('expires_at')

    if not access_token or expires_at <= time.time():
        # Si no hay token de acceso o está vencido, obtener uno nuevo
        access_token, expires_at = obtener_access_token(refresh_token)

        # Almacenar el nuevo token de acceso y su fecha de expiración
        request.session['access_token'] = access_token
        request.session['expires_at'] = expires_at

    return access_token




def obtener_access_token(refresh_token):
    url = "https://oauth2.googleapis.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
         "grant_type": "refresh_token",
          "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
          "client_secret": "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",
         "refresh_token": "1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"
    }

    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    access_token = data["access_token"]
    expires_in = data["expires_in"]
    expires_at = time.time() + expires_in  # Calcula la fecha de expiración

    return access_token, expires_at

def obtener_subcarpetas(folder_id, access_token):
    url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}'+in+parents"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    contenido = response.json()
    subcarpetas = contenido.get("files", [])
   
    return subcarpetas
def obtener_contenido_carpeta(carpeta_id, access_token):
    url = f"https://www.googleapis.com/drive/v3/files?q='{carpeta_id}'+in+parents"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    contenido = response.json()
    subcarpetas = contenido.get("files", [])
   
    return subcarpetas

def administracion(request):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"

    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1bFX5WvZAARs1wyj8wl8L-PAIn3QTlV_c"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'administracion_copy.html', {'subcarpetas': subcarpetas})

def ver_other(request, subcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'other.html', {'subsubcarpetas': subsubcarpetas})

def archivos(request,subsubcarpeta_id):
    refresh_token="1//0h7T0NJuuy8-_CgYIARAAGBESNwF-L9IrxeAh2YORTWnAcJzYOTGo5n5DlcRpGFg_snIwPBJg1jk2X9HGF6N7hVJ9mbY3S08kHWg"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'mostrar_archivos.html', {'archivos': archivos})

def admin(request):
    return render(request, 'admin.html')
