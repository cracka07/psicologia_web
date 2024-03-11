from django.shortcuts import redirect,render

def administracion_academica(request):
    folder_id = "1v1Owd3Rp6JRtpAx0_9bpkn9pFiE0p1SV"

    # Construir la URL de la carpeta de Google Drive
    drive_folder_url = f"https://drive.google.com/drive/folders/{folder_id}"

   
    return render(request,'academy/academy.html')

