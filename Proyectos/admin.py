from django.contrib import admin

# Register your models here.
from Proyectos.models import *


class PortafolioAdmin(admin.ModelAdmin):
    list_display =itemPortafolio
    list_display_links =itemPortafolio

class ImagenesproyectoInline(admin.StackedInline):
    model= Imagenesproyecto
    extra = 1

class ProyectoAdmin(admin.ModelAdmin):
    list_display =itemProyecto
    list_display_links =itemProyecto
    inlines = [ImagenesproyectoInline, ]
    list_filter = ["cliente",]


class ImagenesproyectoAdmin(admin.ModelAdmin):
    list_display =itemImagenesproyecto
    list_display_links =itemImagenesproyecto
    list_filter = ["proyecto__cliente",]


class VisitasproyectoAdmin(admin.ModelAdmin):
    list_display =itemVisitas_Proyecto
    list_display_links = itemVisitas_Proyecto
admin.site.register(Visitas_Proyecto,VisitasproyectoAdmin)

admin.site.register(Portafolio,PortafolioAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Imagenesproyecto,ImagenesproyectoAdmin)


