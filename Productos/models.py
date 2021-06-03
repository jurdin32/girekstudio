from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

# Create your models here.

itemCiudad=['ciudad']
class Ciudad(models.Model):
    ciudad=models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return "%s"%self.ciudad

    class Meta:
        verbose_name_plural = "1. Ciudad"

itemProveedor=['proveedor','logo','detalle','ciudad','direccion','telefono','correo']
class Proveedor(models.Model):
    proveedor=models.CharField(max_length=100, null=True, blank=True)
    logo=models.FileField(upload_to='proveedor/')
    detalle=models.CharField(max_length=300, null=True, blank=True)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    direccion=models.CharField(max_length=100, null=True, blank=True)
    telefono=models.CharField(max_length=100, null=True, blank=True)
    correo=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s"%self.proveedor

    class Meta:
        verbose_name_plural = "2. Proveedor"

itemClasif_producto=['clasificacion_producto']
class Clasif_producto(models.Model):
    clasificacion_producto=models.CharField(max_length=90, null=True, blank=True)

    def __str__(self):
        return "%s"%self.clasificacion_producto

    class Meta:
        verbose_name_plural = "3. Clasificaciòn de Producto"

itemProducto=['vista_previa','clasif','proveedor','nombre_producto','stock','imagen','tamanos','material','precio']
class Producto(models.Model):
    clasif=models.ForeignKey(Clasif_producto,on_delete=models.CASCADE)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    nombre_producto=models.CharField(max_length=100, null=True, blank=True)
    stock=models.CharField(max_length=20, default='stock', choices=(("stock", "stock"), ("no_stock", "no_stock")))
    imagen=models.ImageField(upload_to='producto/')
    descripcion=models.TextField(max_length=500, null=True, blank=True)
    caracteristicas=RichTextField(max_length=500, null=True, blank=True)
    tamanos=models.TextField(max_length=500, null=True, blank=True)
    material=models.TextField(max_length=500, null=True, blank=True)
    precio=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return "%s"%self.nombre_producto

    def vista_previa(self):
        return mark_safe('<image width="100" height="100"  src="/media/%s">' % self.imagen)

    # def vista_previa(self):
    #    if self.imagen:
    #         return """<a href="/media/%s"><img width="48" height="48" border="0" alt="Miniatura" src="/media/%s"/></a>""" % (self.imagen,self.imagen)
    #    else:
    #        return 'No hay imagen'
    #
    # vista_previa.short_description="vista_previa"
    # vista_previa.allow_tags=True

    class Meta:
        verbose_name_plural = "4. Producto"

itemProducto_Imagen=['vista_previa','producto','galeria_articulo']
class Producto_Imagen(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,blank=True, null=True)
    galeria_articulo=models.ImageField(upload_to='media',help_text='imagen producto 800x800',null=True,blank=True)

    def __str__(self):
        return "%s"%self.producto

    def vista_previa(self):
        return mark_safe('<image width="200" height="200"  src="/media/%s">' % self.galeria_articulo)

    class Meta:
        verbose_name_plural='5. Producto Imagenes'
