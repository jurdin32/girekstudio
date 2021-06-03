from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

itemPublicidad=['publi_inicio','publi_servicio','publi_producto','publi_producto2','publi_blog','publi_blog2']
class Publicidad(models.Model):
    publi_inicio=models.FileField(upload_to='publicidad/', help_text="Imagen 1028 x 500")
    publi_servicio=models.FileField(upload_to='publicidad/', help_text="Imagen  x ")
    publi_producto=models.FileField(upload_to='publicidad/', help_text="Imagen  x ")
    publi_producto2=models.FileField(upload_to='publicidad/', help_text="Imagen  x ")
    publi_blog=models.FileField(upload_to='publicidad/', help_text="Imagen  x ")
    publi_blog2=models.FileField(upload_to='publicidad/', help_text="Imagen  x ")
