from django import forms
from .models import Contacto
import re 

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_completo', 'correo_electronico', 'telefono_contacto']
#Agregamos validacion para el Mail
    def clean_correo_electronico(self):
        email = self.cleaned_data.get('correo_electronico')
        pattern = r'^[^ ]+@[^ ]+\.[a-z]{2,3}$'
        if not re.match(pattern, email):
            raise forms.ValidationError("Ingrese un correo electrónico válido")
        return email