from django.shortcuts import render, redirect
from .forms import ContactoForm

# Create your views here.
def formulario_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_exitoso') 
    else:
        form = ContactoForm()

    return render(request, 'eventos/contact.html', {'form': form})