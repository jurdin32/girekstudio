from django.contrib import admin

# Register your models here.
from Productos.models import *


class CiudadAdmin(admin.ModelAdmin):
    list_display = itemCiudad
    list_display_links = itemCiudad

class ProveedorAdmin(admin.ModelAdmin):
    list_display = itemProveedor
    list_display_links = itemProveedor

class Clasif_productoAdmin(admin.ModelAdmin):
    list_display = itemClasif_producto
    list_display_links = itemClasif_producto

class Producto_ImageInline(admin.StackedInline):
    model = Producto_Imagen
    extra = 0

class ProductoAdmin(admin.ModelAdmin):
    list_display = itemProducto
    list_display_links = itemProducto
    inlines = [Producto_ImageInline, ]


class Producto_ImagenAdmin(admin.ModelAdmin):
    list_display = itemProducto_Imagen
    list_display_links = itemProducto_Imagen


admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Clasif_producto,Clasif_productoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Producto_Imagen,Producto_ImagenAdmin)
