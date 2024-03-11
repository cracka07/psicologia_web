from django.shortcuts import render
import folium
# Create your views here.
def address(request):
    initialMap=folium.Map(location=[-31.4365229, -64.1945432],zoom_start=15)
   # Crear un marcador
    marker = folium.Marker(
    location=[-31.4365229, -64.1945432],
    popup=" 'Elma Kohlmeyer de Estrabou' F.F.y H. y Ψ, Avenida Haya de la Torre",
    tooltip=" 'Elma Kohlmeyer de Estrabou' F.F. y H. y Ψ, Avenida Haya de la Torre"

)

    # Añadir el marcador al mapa
    marker.add_to(initialMap)

    context={"map":initialMap._repr_html_()}
    return render(request,"address/address.html",context)