from django.shortcuts import render
# Create your views here.
def doc_psico(request):
   return render(request, 'doc_psico/doc_psico.html')
def unc(request):
    return render(request, 'doc_psico/unc.html')
def unc_publish(request):
    return render(request, 'doc_psico/unc_publish.html')
def unc_ffyh(request):
    return render(request, 'doc_psico/unc_ffyh.html')
