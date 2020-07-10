from django.contrib import admin

# Register your models here.
from Empresa.models import *

class LogotipoAdmin(admin.ModelAdmin):
    list_display = itemLogotipo
    list_display_links = itemLogotipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = itemEquipo
    list_display_links = itemEquipo

class MiviAdmin(admin.ModelAdmin):
    list_display =itemMivi
    list_display_links =itemMivi

class ValoresAdmin(admin.ModelAdmin):
    list_display = itemValores
    list_display_links = itemValores


class ProcesoAdmin(admin.ModelAdmin):
    list_display =itemProceso
    list_display_links =itemProceso

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = itemsExperiencia
    list_display_links = itemsExperiencia

class Contacto_empresaAdmin(admin.ModelAdmin):
    list_display = itemContacto_empresa
    list_display_links = itemContacto_empresa

class Contacto_redesAdmin(admin.ModelAdmin):
    list_display=itemContacto_redes
    list_display_links = itemContacto_redes

admin.site.register(Logotipo,LogotipoAdmin)
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Mivi,MiviAdmin)
admin.site.register(Valores,ValoresAdmin)
admin.site.register(Proceso,ProcesoAdmin)
admin.site.register(Experiencia,ExperienciaAdmin)
admin.site.register(Contacto_empresa,Contacto_empresaAdmin)
admin.site.register(Contacto_redes,Contacto_redesAdmin)
