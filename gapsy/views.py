from django.shortcuts import render
import folium

def home(request):
    return render(request,"inicio.html")

def contact(request):
    initialMap=folium.Map(location=[-31.43712114114905, -64.18951891634443],zoom_start=15)
   # Crear un marcador
    marker = folium.Marker(location=[-31.43712114114905, -64.18951891634443], popup="Facultad de Psicología")

    # Añadir el marcador al mapa
    marker.add_to(initialMap)

    context={"map":initialMap._repr_html_()}
    return render(request,"contacto.html",context)

def about(request):
    return render(request,"about.html")

def objetivos(request):
    return render(request,"objetivos.html")