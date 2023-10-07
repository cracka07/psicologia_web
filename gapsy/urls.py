
from django.conf import  settings
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="home"),
    path("contacto/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("document/",include("recursos.urls")),
    path("document_al/",include("alumnos.urls")),
    path("document_msc/",include("miscelanea.urls")),
    path("document_docacademica/",include("docacademica.urls")),
     path("document_docinvest/",include("docinvestigacion.urls")),
      path("document_docjuridica/",include("docjuridica.urls")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

