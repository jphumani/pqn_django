from django.db import models

# Create your models here.

class Evento(models.Model):
    title = models.CharField(max_length=500,verbose_name="Título de Evento")
    description = models.TextField(verbose_name="Descripción")
    picture = models.ImageField(verbose_name="Imagen",upload_to="eventos") #pongo nombre de la app que declare
    created = models.DateField(auto_now_add=True,verbose_name="Fecha subido")
    updated = models.DateField(auto_now=True, auto_now_add=False,verbose_name="Ultima actualización")
    
    #Con esto resuelvo que el nombre sea que crea el usuario.
    def __str__(self) -> str:
        return self.title
    
class Contacto(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField(primary_key=True)
    telefono_contacto = models.CharField(max_length=15)
    def __str__(self):
        return "{} {}".format(self.nombre_completo, self.correo_electronico)