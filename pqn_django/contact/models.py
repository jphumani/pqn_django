from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=20,  verbose_name="Teléfono de Contacto")
    message = models.TextField(verbose_name = "Mensaje")
    created = models.DateField(auto_now_add=True,verbose_name="Fecha de Envio")
