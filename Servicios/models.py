from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


itemServicio=['vista_previa','orden','imagen','titulo']
class Servicio(models.Model):
    orden=models.IntegerField()
    imagen=models.ImageField(upload_to='servicio/' ,null=True,blank=True)
    titulo=models.TextField()
    descripcion=models.TextField()
    def __str__(self):

        return self.titulo

    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "1. Servicio"

itemInfoicono=['nombre']
class Infoicono(models.Model):
    nombre=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "5.Icono Info Servicio"

itemInfoserv=['infoicono','servicio','titulo','descripcion']
class Infoserv (models.Model):
    infoicono=models.ForeignKey(Infoicono,on_delete=models.CASCADE)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    titulo=models.TextField(default="")
    descripcion=models.TextField(default="")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "4. Info Servicio"

itemImagenesServicio=['vista_previa','servicio','imagen','estado']
class ImagenesServicio(models.Model):
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    imagen=models.FileField(upload_to='servicio/')
    estado=models.BooleanField(default=False)

    def vista_previa(self):
        return mark_safe('<image width="150" height="150"  src="/media/%s">' % self.imagen)

    class Meta:
        verbose_name_plural = "2. Imagenes Servicio "



itemVideoServicio=['servicio','video']
class VideoServicio(models.Model):
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE)
    video=models.FileField(upload_to='servicio/')


itemTipo_plan=['plan']
class Tipo_plan(models.Model):
    plan=models.CharField(max_length=1, null=True,blank=True, help_text=" A,B,C,D")

    def __str__(self):
        return self.plan

itemContenido_plan=['tipo_plan','servicio','planpopular','precioplan']
class Contenido_plan(models.Model):
    tipo_plan=models.ForeignKey(Tipo_plan,on_delete=models.CASCADE , null=True,blank=True)
    servicio=models.ForeignKey(Servicio,on_delete=models.CASCADE, null=True,blank=True)
    planpopular=models.BooleanField(default=False)
    precioplan=models.CharField(max_length=60, null=True,blank=True)



    def __str__(self):
        return self.servicio.titulo

itemDetalle_plan=['detalle','contenido']
class Detalle_plan(models.Model):
    detalle=models.CharField(max_length=60)
    contenido=models.ForeignKey(Contenido_plan,on_delete=models.CASCADE)
    def __str__(self):
        return self.detalle
