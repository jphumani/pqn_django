from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('contact')+'?ok')
        else:
            return redirect(reverse('contact')+'?error')            
            
    return render(request,"core/pages/contact.html", {"form":contact_form})

