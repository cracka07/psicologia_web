
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

# def galeria(request):
#     picture_id='1PLIcLC6Xkor4xkp9WQFEJhph3EcPN1-4'
#     visor_picture=f'https://drive.google.com/embeddedfolderview?id={picture_id}#grid'
#     context={
#         "visor_picture":visor_picture
#     }
#     return render(request,"galery.html",context)
    