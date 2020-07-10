from django.contrib import admin

# Register your models here.
from Publicidad.models import *


class PublicidadAdmin(admin.ModelAdmin):
    list_display = itemPublicidad
    list_display_links = itemPublicidad

admin.site.register(Publicidad,PublicidadAdmin)