# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe

itemSlider=['vista_previa','orden','tipo_archivo','archivo','titulo','subtitulo']
class Slider(models.Model):
    orden=models.IntegerField()
    archivo=models.FileField(upload_to='slider/',help_text='imagen de 1920*529')
    titulo=models.TextField()
    subtitulo = models.TextField(null=True,blank=True)
    tipo_archivo=models.CharField(max_length=20, default='imagen', choices=(("imagen", "imagen"), ("video", "video")))

    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.archivo)

itemTrabajo=['fecha_subida','imagen']
class Trabajo(models.Model):
    fecha_subida=models.DateField(auto_now_add=True)
    imagen=models.FileField(upload_to='trabajo/')



itemCliente=['vista_previa','orden','nombre','sitio','logo']
class Cliente(models.Model):
    orden=models.IntegerField()
    nombre=models.TextField()
    sitio=models.TextField(null=True,blank=True)
    logo=models.FileField(upload_to='logocliente/')

    def __str__(self):
        return  self.nombre

    def vista_previa(self):
        return mark_safe('<image width="250" height="80"  src="/media/%s">' % self.logo)


itemFrase=['cita','autor']
class Frase(models.Model):
    cita=models.TextField()
    autor=models.TextField()



