from django.shortcuts import render

# Create your views here.
def index_base(request):
    return render(request,"core/index_base.html")

def index(request):
    return render(request,"core/index.html")

def austral(request):
    return render(request,"core/pages/austral.html")

def centro(request):
    return render(request,"core/pages/centro.html")

def patagonia(request):
    return render(request,"core/pages/patagonia.html")

def noroeste(request):
    return render(request,"core/pages/noroeste.html")

def noreste(request):
    return render(request,"core/pages/noreste.html")

def mar(request):
    return render(request,"core/pages/mar.html")

def map(request):
    return render(request,"core/pages/map.html")
