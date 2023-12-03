
from django.shortcuts import redirect, render
import requests


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
    folder_id = "1bFX5WvZAARs1wyj8wl8L-PAIn3QTlV_c"

    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

   
    return redirect(drive_folder_url)

def admin(request):
    return render(request, 'admin.html')
