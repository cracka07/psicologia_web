from django.http import HttpResponse
from django.shortcuts import render
import requests
import requests





def obtener_access_token(refresh_token):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"
    url = "https://oauth2.googleapis.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "client_id": "1070121079619-6jf8abittdbhlgtrpu005nplbivf4mll.apps.googleusercontent.com",
        "client_secret": "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",  # Reemplaza con tu client secret
        "refresh_token": refresh_token
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

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
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"
    access_token = obtener_access_token(refresh_token)
    folder_id = "1dbUh5OIMTEbJyJbhvVR66DuzNSmfZy7l"

    subcarpetas = obtener_subcarpetas(folder_id, access_token)

    return render(request, 'administracion_copy.html', {'subcarpetas': subcarpetas})

def ver_other(request, subcarpeta_id):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"

    access_token = obtener_access_token(refresh_token)
    subsubcarpetas = obtener_contenido_carpeta(subcarpeta_id, access_token)
 
    
    return render(request, 'other.html', {'subsubcarpetas': subsubcarpetas})

def archivos(request,subsubcarpeta_id):
    refresh_token="1//0hm5HgEoEqFYNCgYIARAAGBESNwF-L9IrDC-1jr44_LUZ6QQGt6wfkN7bDIFm0IU0JaKDxwQ_DrvvUGG3qIb640p-FtcjQSfsahA"

    access_token = obtener_access_token(refresh_token)
    archivos = obtener_contenido_carpeta(subsubcarpeta_id, access_token)
  
    return render(request, 'mostrar_archivos.html', {'archivos': archivos})

def admin(request):
    return render(request, 'admin.html')
