
from django.shortcuts import redirect,render

def admin(request):
   
    return render(request,'administrativo/admin.html')

def doc_alumnos(request):
   
    return render(request,'administrativo/doc_alumnos.html')

def doc_docentes(request):
   
    return render(request,'administrativo/doc_docentes.html')

def doc_compras(request):
   
    return render(request,'administrativo/doc_compras.html')




    