from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def Contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data= request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            #Aviso que el fomulario se envio ok
            return redirect(reverse('contact')+ '?ok')
        else:
            #Genero un error
            return redirect(reverse('contact')+ '?error')
    
    return render(request, 'contact/contact.html', {'form' :contact_form}) 