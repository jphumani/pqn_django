from django.db import models

# Create your models here.
options= [
    [0, 'Pedido de información'],
    [1, 'Comentarios/Sugerencias'],
    [2, 'Queja/Reclamo'],
    [3, 'Otro']
]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    lastname = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo electronico')
    contact_type = models.IntegerField(choices= options, verbose_name= 'Tipo de Contacto')
    message = models.TextField(verbose_name= 'Mensaje')
    subscription = models.BooleanField(default= False, verbose_name='Suscribirme a Newsletter')
    created_at = models.DateTimeField(auto_now_add= True, verbose_name='Fecha de envio')