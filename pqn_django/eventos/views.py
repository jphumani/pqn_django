from django.shortcuts import render
from .models import Evento

# Create your views here.
def servicios(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/servicios.html", {'eventos':eventos})
