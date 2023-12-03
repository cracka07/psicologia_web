from django.shortcuts import redirect

def administracion_miscelanea(request):
    folder_id = "1JuZdzpu84Uh1pIsxvUqa8Q4hyGahr1gt"

    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

    return redirect(drive_folder_url)
