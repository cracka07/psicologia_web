from django.shortcuts import render


def home(request):
    return render(request,"inicio.html")




def about(request):
    return render(request,"about.html")

def objetivos(request):
    return render(request,"objetivos.html")