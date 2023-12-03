from django.shortcuts import redirect

def administracion_juri(request):
    folder_id = "1yOQt5Yfn4QHEf8Cm1ghR-WBfRCe6t5ct"

    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

   
    return redirect(drive_folder_url)

