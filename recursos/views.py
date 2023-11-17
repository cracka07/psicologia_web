

import time
from django.shortcuts import render



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from requests import RequestException
import requests
# # Ruta al archivo JSON de la cuenta de servicio
# SERVICE_ACCOUNT_FILE = 'service_account.json'

# # Cargar las credenciales desde el archivo JSON
# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive']
# )

# # Obtener un token de acceso
# credentials.refresh(Request())

# # Ahora, credentials contiene el token de acceso y el token de actualización
# access_token = credentials.token
# refresh_token = credentials.refresh_token

def obtener_o_renovar_access_token(request, refresh_token):
    try:
        access_token = request.session.get('access_token')
        expires_at = request.session.get('expires_at')

        if not access_token or expires_at <= time.time():
            # Si no hay token de acceso o está vencido, obtener uno nuevo
            access_token, expires_at, new_refresh_token = obtener_access_token(refresh_token)

            # Almacenar el nuevo token de acceso y su fecha de expiración
            request.session['access_token'] = access_token
            request.session['expires_at'] = expires_at

            # Actualizar el refresh_token si se emite uno nuevo
            if new_refresh_token:
                request.session['refresh_token'] = new_refresh_token

        return access_token
    except RequestException as e:
        # Manejar la excepción de red u otros errores aquí
        print(f"Error al obtener/renovar el token de acceso: {str(e)}")
        return None

def obtener_access_token(refresh_token):
    try:
        url = "https://oauth2.googleapis.com/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "refresh_token",
            "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
            "client_secret": "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",
            "refresh_token": refresh_token
        }

        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Lanza una excepción si la respuesta indica un error HTTP

        data = response.json()
        access_token = data["access_token"]
        expires_in = data["expires_in"]
        expires_at = time.time() + expires_in  # Calcula la fecha de expiración

        # Verificar si se emitió un nuevo refresh_token
        new_refresh_token = data.get("refresh_token")

        return access_token, expires_at, new_refresh_token
    except RequestException as e:
        # Manejar la excepción de red u otros errores aquí
        print(f"Error al obtener el token de acceso: {str(e)}")
        print(f"Respuesta HTTP: {response.status_code} - {response.text}")
        return None, None, None



# Ruta al archivo JSON de la cuenta de servicio
SERVICE_ACCOUNT_FILE = 'client_secrets.json'

# Cargar las credenciales desde el archivo JSON



gauth = GoogleAuth()
gauth.service_account_file = SERVICE_ACCOUNT_FILE
drive = GoogleDrive(gauth)

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
    refresh_token="1//0h3pQxZ468uI7CgYIARAAGBESNwF-L9IrwPUfoModZ4tk2NxbdJl_219ZOYg_FwLeLBuxpzVwbLtTlESTwRTALODr5aoyKn1OX8I"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    folder_id = "1bFX5WvZAARs1wyj8wl8L-PAIn3QTlV_c"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'administracion_copy.html', {'subcarpetas': subcarpetas})

def ver_other(request, subcarpeta_id):
    refresh_token="1//0h3pQxZ468uI7CgYIARAAGBESNwF-L9IrwPUfoModZ4tk2NxbdJl_219ZOYg_FwLeLBuxpzVwbLtTlESTwRTALODr5aoyKn1OX8I"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'other.html', {'subsubcarpetas': subsubcarpetas})

def archivos(request,subsubcarpeta_id):
    refresh_token="1//0h3pQxZ468uI7CgYIARAAGBESNwF-L9IrwPUfoModZ4tk2NxbdJl_219ZOYg_FwLeLBuxpzVwbLtTlESTwRTALODr5aoyKn1OX8I"
    access_token = obtener_o_renovar_access_token(request, refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'mostrar_archivos.html', {'archivos': archivos})

def admin(request):
    return render(request, 'admin.html')
