
from django.shortcuts import redirect,render

def administracion(request):
    # Definir el ID de la carpeta de Google Drive que se va a enlazar
    folder_id = "1bFX5WvZAARs1wyj8wl8L-PAIn3QTlV_c"
    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
    # Redirigir al usuario a la URL de la carpeta de Google Drive
    return redirect(drive_folder_url)

def admin(request):
    return render(request, 'admin.html')
