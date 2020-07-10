from django.db import models

# Create your models here.
from Inicio.models import *
from django.utils.safestring import mark_safe


itemPortafolio=['portafolio','visualizaciones']
class Portafolio(models.Model):
    portafolio=models.TextField()
    visualizaciones=models.IntegerField(default=1)

    def save(self, *args,**kwargs):
        self.visualizaciones+=1
        super(Portafolio,self).save(*args, **kwargs)

    def __str__(self):

        return  self.portafolio

    class Meta:
        verbose_name_plural = "1. Tema Protafolio"

itemProyecto=['orden','vista_previa','portafolio','cliente','fecha','nombreproyecto','detalle','tipo_archivo','imagen','link']
class Proyecto(models.Model):
    orden=models.IntegerField(default=0)
    portafolio=models.ForeignKey(Portafolio,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha=models.DateField()
    nombreproyecto=models.CharField(max_length=120, null=True,blank=True, help_text="Texto de maximo 120 caracteres")
    detalle=models.TextField(null=True,blank=True)
    tipo_archivo=models.CharField(max_length=20,default='imagen',choices=(("imagen","imagen"),("video_vertical","video_vertical"),("video","video")))
    imagen=models.FileField(upload_to='portafolio/',help_text='imagen producto 851x315',null=True,blank=True)
    link=models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):

        return '%s %s'% (self.nombreproyecto,self.cliente)

    def vista_previa(self):
        return mark_safe('<image width="250" height="100"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "2. Proyecto"


itemImagenesproyecto=['vista_previa','proyecto','galeriaproyecto']
class Imagenesproyecto(models.Model):
    proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    galeriaproyecto=models.FileField(upload_to='galeriaproyecto/')


    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.galeriaproyecto)

    class Meta:
        verbose_name_plural = "3. Proyecto Imagenes"



itemVisitas_Proyecto=['proyecto','visita']
class Visitas_Proyecto(models.Model):
    proyecto=models.OneToOneField(Proyecto,on_delete=models.CASCADE ,null=True,blank=True)
    visita=models.IntegerField(default=1)

    def visitar(self):
        return "<a target='blank' href='http://www.girekstudio.com/proyecto/%s'>Ver en la Web</a>" % self.proyecto.id

    visitar.allow_tags = True
    visitar.short_description = "Ir"

    def save(self, *args, **kwargs):
        self.visita += 1
        super(Visitas_Proyecto, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "4. Visitas al Proyecto"