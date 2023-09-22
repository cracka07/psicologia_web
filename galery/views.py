from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.conf import settings
import os

def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image = request.FILES['image']
        with open(os.path.join(settings.MEDIA_ROOT, image.name), 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

    image_files = [f for f in os.listdir(settings.MEDIA_ROOT) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    images = [os.path.join(settings.MEDIA_URL, f) for f in image_files]

    return render(request, 'gallery.html', {'images': images})

# from django.shortcuts import render, redirect

# from galery.forms import ImageUploadForm

# def upload_image(request):
#     if request.method == 'POST':
#         # Verifica si el formulario es válido
#         form = ImageUploadForm(request.POST, request.FILES)  # Reemplaza YourImageForm con el nombre de tu formulario

#         if form.is_valid():
#             # Procesa la imagen aquí
#             # La imagen estará disponible en request.FILES['image']
#             # Por ejemplo, para guardarla en la carpeta media/ puedes hacer lo siguiente:

#             image = request.FILES['image']
#             with open('media/' + image.name, 'wb+') as destination:
#                 for chunk in image.chunks():
#                     destination.write(chunk)

#             return redirect('upload_image')  # Redirige a la página de la galería después de subir la imagen

#     else:
#         form =ImageUploadForm()  # Reemplaza YourImageForm con el nombre de tu formulario

#     return render(request, 'gallery.html', {'form': form})


