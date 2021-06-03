from django.contrib import admin

# Register your models here.
from Inicio.models import *


class SliderAdmin(admin.ModelAdmin):
    list_display =itemSlider
    list_display_links = itemSlider

class TrabajoAdmin(admin.ModelAdmin):
    list_display = itemTrabajo
    list_display_links =itemTrabajo

class ClienteAdmin(admin.ModelAdmin):
    list_display = itemCliente
    list_display_links = itemCliente


class FraseAdmin(admin.ModelAdmin):
    list_display =itemFrase
    list_display_links =itemFrase



admin.site.register(Slider,SliderAdmin)
admin.site.register(Trabajo,TrabajoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Frase,FraseAdmin)



