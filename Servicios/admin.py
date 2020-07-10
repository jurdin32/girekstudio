from django.contrib import admin

# Register your models here.

from Servicios.models import *

class InfoservAdmin(admin.ModelAdmin):
    list_display =itemInfoserv
    list_display_links =itemInfoserv


class InfoiconoAdmin(admin.ModelAdmin):
    list_display =itemInfoicono
    list_display_links =itemInfoicono

class ServicioAdmin(admin.ModelAdmin):
    list_display =itemServicio
    list_display_links =itemServicio

class ImagenesServicioAdmin(admin.ModelAdmin):
    list_display = itemImagenesServicio
    list_display_links = itemImagenesServicio

class VideoServicioAdmin(admin.ModelAdmin):
    list_display = itemVideoServicio
    list_display_links = itemVideoServicio

class Detalle_inLine(admin.StackedInline):
    model = Detalle_plan
    extra = 1

class Contenido_planAdmin(admin.ModelAdmin):
    list_display = itemContenido_plan
    list_display_links = itemContenido_plan
    list_filter = ['tipo_plan','servicio']
    inlines = [Detalle_inLine]

class Tipo_planAdmin(admin.ModelAdmin):
    list_display = itemTipo_plan
    list_display_links = itemTipo_plan

admin.site.register(Infoserv,InfoservAdmin)
admin.site.register(Infoicono,InfoiconoAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(ImagenesServicio,ImagenesServicioAdmin)
admin.site.register(VideoServicio,VideoServicioAdmin)
admin.site.register(Contenido_plan,Contenido_planAdmin)
admin.site.register(Tipo_plan,Tipo_planAdmin)



