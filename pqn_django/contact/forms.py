from django import forms 
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'lastname', 'email', 'contact_type', 'message', 'subscription']