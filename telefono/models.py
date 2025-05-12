from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True, verbose_name='Correo Electrónico')
    foto = models.ImageField(upload_to='contactos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email}"
    
    class Meta:
        permissions = (
            ('puede_ver_contactos', 'Ver contactos'),
            ('puede_escribir_contactos', 'Escribir contactos')   
        )
        