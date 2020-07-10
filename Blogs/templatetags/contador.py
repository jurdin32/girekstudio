from django import template

from Blogs.models import Visitas_Blog
from Proyectos.models import Visitas_Proyecto
register=template.Library()

@register.simple_tag
def vistanumero(id):
    numero=0
    try:
        numero=Visitas_Blog.objects.get(blog_id=id).visita
    except:
        numero=0
    return numero

@register.simple_tag
def vistanumeropro(id):
    numeros=0
    try:
        numero=Visitas_Proyecto.objects.get(proyecto_id=id).visita
    except:
        numero=0
    return numero