
from django.shortcuts import  render
import os

# Create your views here.
def activity(request):
   
    # Obtener la lista de archivos en la carpeta uploads
    imagenes = [f for f in os.listdir("uploads") if os.path.isfile(os.path.join("uploads", f))]

    return render(request,'activity/activities.html', {'imagenes': imagenes})


# def eliminar_imagen(request):
#     if request.method == 'POST':
#         imagen = request.POST.get('imagen', None)
#         if imagen:
#             # Ruta completa del archivo de imagen
#             ruta_imagen = os.path.join("uploads", imagen)
#             # Eliminar la imagen del sistema de archivos
#             if os.path.exists(ruta_imagen):
#                 os.remove(ruta_imagen)
#     return redirect('activities')



# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Create the directory uploads if it doesn't exist
#             if not os.path.exists('uploads'):
#                 os.makedirs('uploads')

#             with open('uploads/' + request.FILES['file'].name, 'wb+') as destination:
#                 for chunk in request.FILES['file'].chunks():
#                     destination.write(chunk)
# # Construct the MEDIA_URL prefix for images
#             image_url = f'{MEDIA_URL}{request.FILES["file"].name}'
#             image_files = [f for f in os.listdir('uploads') if f.endswith(('.jpg', '.jpeg', '.png'))]
#             context = {'image_url': image_url, 'image_files': image_files}
#             return redirect('activities')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

