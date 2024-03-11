
from django.conf import  settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="home"),

    path("about/",views.about,name="about"),
    path("document/",include("recursos.urls")),
    # path("document_al/",include("alumnos.urls")),
    # path("document_msc/",include("miscelanea.urls")),
    path("direccion/",include("direccion.urls")),  
    path("actividad/",include("actividades.urls")),  
    path("document_docacademica/",include("docacademica.urls")),
     path("document_docinvest/",include("docinvestigacion.urls")),
      path("document_docjuridica/",include("docjuridica.urls")),
        path("document_psicoanalisis/",include("doc_psico.urls")),
      
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

