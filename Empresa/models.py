from django.db import models

# Create your models here.
from Inicio.models import *
from django.utils.safestring import mark_safe

itemEquipo=['imagen','nombre','cargo','correo','facebook','twitter','linkedin','vista_previa']
class Equipo(models.Model):
    imagen=models.FileField(upload_to='equipo/')
    nombre=models.TextField()
    cargo=models.TextField()
    correo=models.EmailField()
    facebook=models.TextField(default='http://www.facebook.com/')
    twitter=models.TextField( default='http://www.twitter.com/')
    linkedin=models.TextField(default='http://www.linkedin.com/')

    def vista_previa(self):
        return mark_safe('<image width="300" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "4. Equipo de Trabajo"



itemMivi=['mision','vision']
class Mivi(models.Model):
    mision=models.TextField(max_length=400,null=True,blank=True)
    vision=models.TextField(max_length=400,null=True,blank=True)

    class Meta:
        verbose_name_plural = "2. Misión / Visión"

itemValores=['icono','valor','concep_valor']
class Valores(models.Model):
    icono=models.CharField(max_length=9,null=True,blank=True)
    valor=models.CharField(max_length=25,null=True,blank=True)
    concep_valor=models.TextField(max_length=300,null=True,blank=True)

    class Meta:
        verbose_name_plural = "3. Valores"

itemsExperiencia=['clientes','experiencia','reconocimientos','certificaciones']
class Experiencia(models.Model):
    clientes=models.CharField(max_length=3,null=True,blank=True)
    experiencia=models.CharField(max_length=3,null=True,blank=True)
    reconocimientos=models.CharField(max_length=3,null=True,blank=True)
    certificaciones=models.CharField(max_length=3,null=True,blank=True)

    class Meta:
        verbose_name_plural = "5.  Experiencia"

itemProceso=['tema_uno','tema_dos','tema_tres','tema_cuatro']
class Proceso(models.Model):
    tema_uno=models.TextField()
    tema_dos=models.TextField()
    tema_tres=models.TextField()
    tema_cuatro=models.TextField()

    class Meta:
        verbose_name_plural = "6. Proceso"

itemLogotipo=['logo','logo_blanco','logo_blanco2','logo_negro','favicon']
class Logotipo(models.Model):
    logo=models.ImageField(upload_to='empresa/logo/')
    logo_blanco=models.ImageField(upload_to='empresa/logo/')
    logo_blanco2=models.ImageField(upload_to='empresa/logo/')
    logo_negro=models.ImageField(upload_to='empresa/logo/')
    favicon=models.ImageField(upload_to='empresa/logo/')

    class Meta:
        verbose_name_plural = "1. Logotipo"




itemContacto_empresa=['direccion','calle','mapa','representante','correo_personal','celular','celular2','telefono','correo']
class Contacto_empresa(models.Model):
    direccion=models.CharField(max_length=100,null=True,blank=True)
    calle=models.CharField(max_length=100,null=True,blank=True)
    mapa=models.TextField(max_length=500,null=True,blank=True)
    representante=models.CharField(max_length=100, null=True,blank=True)
    correo_personal=models.CharField(max_length=100, null=True,blank=True)
    celular=models.CharField(max_length=11,null=True,blank=True)
    celular2=models.CharField(max_length=100,null=True,blank=True)
    telefono=models.CharField(max_length=15,null=True,blank=True)
    correo=models.EmailField()

    class Meta:
        verbose_name_plural = "7. Contácto"

itemContacto_redes=['facebook','instagram','twitter','linkedin','youtube','behance']
class Contacto_redes(models.Model):
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    behance = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "8. Contácto Redes Sociales"
