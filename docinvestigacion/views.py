from django.shortcuts import redirect

def administracion_invest(request):
    folder_id = "1axJ3Yb0BrgJ7YKCp34K8peSE_HuV_6AE"

    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

   
    return redirect(drive_folder_url)

