# encoding: utf-8
from django.core.mail import EmailMultiAlternatives
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response

from Empresa.models import *
from Productos.models import *
from Proyectos.models import *
from Blogs.models import *
from Publicidad.models import *
from Servicios.models import *
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def blog_paginado(request):
    list = Blogs.objects.all().order_by("-fecha")
    paginator = Paginator(list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        blogss = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogss = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogss = paginator.page(paginator.num_pages)
    return blogss


def index(request):
    contexto = {'logotipo': Logotipo.objects.all(),
                'sliders': Slider.objects.all().order_by("orden"),
                'trabajos': Proyecto.objects.all().order_by('orden'),
                'clientes': Cliente.objects.all().order_by("orden"),
                'servicio': Servicio.objects.all().order_by("orden"),
                'imagenes': ImagenesServicio.objects.all(),
                'blog': Blogs.objects.all().order_by("-fecha"),
                'iconos': Infoicono.objects.first(),
                'contacto_empresa': Contacto_empresa.objects.all(),
                'contacto_redes': Contacto_redes.objects.get(),
                'publicidad': Publicidad.objects.all(),
                }
    return render_to_response("demo-digital-agency.html", contexto)


def estudio(request):
    contexto = {
        'equipos': Equipo.objects.all(),
        'clientes': Cliente.objects.all(),
        'mivi': Mivi.objects.get(),
        'valores': Valores.objects.all(),
        'experiencias': Experiencia.objects.all(),
        'frases': Frase.objects.all(),
        'contacto_empresa': Contacto_empresa.objects.all(),
        'contacto_redes': Contacto_redes.objects.get(),
    }

    try:
        mivi = Mivi.objects.first()
    except:
        mivi = None
    return render_to_response("demo-digital-agency-about.html", contexto)


def servicios(request):
    servicio = Servicio.objects.all().order_by("orden")
    imagenes = ImagenesServicio.objects.all()
    contacto_empresa = Contacto_empresa.objects.all()
    contacto_redes = Contacto_redes.objects.get()
    try:
        proceso = Proceso.objects.first()
    except:
        proceso = None
    return render_to_response("demo-digital-agency-services.html",
                              {"servicios": servicio, "imagenes": imagenes, "proceso": proceso,
                               "contacto_empresa": contacto_empresa, "contacto_redes": contacto_redes})


def serviciosdescripcion(request, n):
    servicio = Servicio.objects.get(id=n)
    imagenes = ImagenesServicio.objects.filter(servicio=servicio)
    videoserv = VideoServicio.objects.filter(servicio=servicio)
    infoserv = Infoserv.objects.filter(servicio=servicio)
    contacto_empresa = Contacto_empresa.objects.all()
    contenido_plan = Contenido_plan.objects.filter(servicio_id=n)
    detalles = Detalle_plan.objects.all()
    contacto_redes = Contacto_redes.objects.get()

    return render_to_response("demo-digital-agency-description-services.html",
                              {"servicios": servicio, "imagenes": imagenes, "videoserv": videoserv,
                               "infoserv": infoserv, "contacto_empresa": contacto_empresa, "planes": contenido_plan,
                               "detalles": detalles, "contacto_redes": contacto_redes})


def portafolio(request):
    visitas = Visitas_Proyecto.objects.all()
    proyectos = Proyecto.objects.all().order_by('orden')
    portafolios = Portafolio.objects.all()
    clientes = Cliente.objects.all()
    contacto_empresa = Contacto_empresa.objects.all()
    contacto_redes = Contacto_redes.objects.get()
    return render_to_response("demo-digital-agency-work.html",
                              {"visitas": visitas, "proyectos": proyectos, "portafolios": portafolios,
                               "clientes": clientes, "contacto_empresa": contacto_empresa,
                               "contacto_redes": contacto_redes})


def portafolioimagen(request, n):
    proyecto = Proyecto.objects.get(id=n)
    portaf = Proyecto.objects.get(id=n)
    imagenesproyecto = Imagenesproyecto.objects.filter(proyecto=proyecto)
    contacto_empresa = Contacto_empresa.objects.all()
    contacto_redes = Contacto_redes.objects.get()
    try:
        pt = Visitas_Proyecto.objects.get(proyecto_id=n)
        pt.save()
    except:
        Visitas_Proyecto(proyecto_id=n).save()
    return render_to_response("demo-digital-agency-work-detail.html",
                              {"proyecto": proyecto, "portaf": portaf, "imagenesproyecto": imagenesproyecto,
                               "contacto_empresa": contacto_empresa, "contacto_redes": contacto_redes})


def tienda(request):
    contexto = {
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.all().order_by('-id'),
        'contacto_empresa': Contacto_empresa.objects.all(),
        'contacto_redes': Contacto_redes.objects.get(),
        'publicidad': Publicidad.objects.all(),

    }
    return render_to_response('demo-digital-tienda.html', contexto)


def producto_cate(request, id):
    contexto = {
        'categorias': Clasif_producto.objects.all(),
        'productos': Producto.objects.filter(clasif_id=id),
        'contacto_empresa': Contacto_empresa.objects.all(),
        'contacto_redes': Contacto_redes.objects.get(),
        'publicidad': Publicidad.objects.all(),
    }
    return render_to_response('demo-digital-tienda.html', contexto)


def producto_id(request, n):
    product = Producto.objects.get(id=n)
    producto_imagen = Producto_Imagen.objects.filter(producto=product)
    contacto_empresa = Contacto_empresa.objects.all()
    contacto_redes = Contacto_redes.objects.get()
    print(product.imagen)
    return render_to_response('demo-digital-product.html', {'product': product, 'producto_imagen': producto_imagen,
                                                            'contacto_empresa': contacto_empresa,
                                                            'contacto_redes': contacto_redes})


def blog(request):
    contexto = {
        'blog': blog_paginado(request),
        'visitas': Visitas_Blog.objects.all(),
        'blogs': Blogs.objects.all().order_by('-id'),
        'categorias': Categoria.objects.all(),
        'paginas': "x" * blog_paginado(request).paginator.num_pages,
        'contacto_empresa': Contacto_empresa.objects.all(),
        'contacto_redes': Contacto_redes.objects.get(),
        'publicidad': Publicidad.objects.all(),
    }

    return render_to_response("demo-digital-blog-medium-image.html", contexto)


def blogfiltradocategoria(request, n):
    cat = Categoria.objects.get(id=n)
    blogg = Blogs.objects.filter(categoria=cat)
    categorias = Categoria.objects.all()
    contacto_empresa = Contacto_empresa.objects.all()
    contacto_redes = Contacto_redes.objects.get()
    return render_to_response("demo-digital-blog-medium-image.html",
                              {"blogs": blogg, "categorias": cat, "cats": categorias,
                               "contacto_empresa": contacto_empresa, "contacto_redes": contacto_redes})


def post(request, n):
    try:
        Visitas_Blog(blog_id=n).save()
    except:
        visita = Visitas_Blog.objects.get(blog_id=n)
        visita.save()
    blogg = Blogs.objects.get(id=n)
    if request.POST:
        if len(request.POST['comment']) > 0:
            pregunta = Comentario(blog=blogg, pregunta=request.POST['comment'], usuario=request.POST['name'],
                                  email=request.POST['email'])
            pregunta.save()
            enviar_email(request, 'Comentarios de Blog', request.POST['name'] + '<' + request.POST['email'] + '>',
                         'info@girekstudio.com',
                         'Un usuario ha publicado una entrada en el blog, con el texto. >>' + request.POST['comment'])
            enviar_email(request, 'Info GirekStudio', 'info@girekstudio.com',
                         request.POST['name'] + '<' + request.POST['email'] + '>',
                         u'Su comentario fué publicado >>' + request.POST['comment'])
        return HttpResponseRedirect("/post/" + n + "/")
    else:
        preguntas = Comentario.objects.filter(blog=blogg)
        respuestas = Respuesta.objects.all()
        contador = Comentario.objects.all()
        return render_to_response("demo-digital-post.html", {
            "blog": blogg, "comentarios": preguntas, "respuestas": respuestas, "contador": contador.count(),
            "blogs": Blogs.objects.all().order_by("-fecha")[:20],
        })


# postear una respuesta
def postrespuesta(request, n, idBlog):
    if request.POST:
        bloger = Comentario.objects.get(id=n)
        respuesta = Respuesta(comentario=bloger, usuario=request.POST['usuario'], respuesta=request.POST['respuesta'],
                              email=request.POST['email'])
        respuesta.save()
        enviar_email(request, 'Comentarios de Blog', request.POST['usuario'] + '<' + request.POST['email'] + '>',
                     'info@girekstudio.com',
                     'Un usuario ha publicado una entrada en el blog, con el texto. >>' + request.POST['respuesta'])
        enviar_email(request, 'Info GirekStudio', 'info@girekstudio.com',
                     request.POST['usuario'] + '<' + request.POST['email'] + '>',
                     'Su comentario fué publicado >>' + request.POST['respuesta'])
        return HttpResponseRedirect("/post/" + idBlog + "/")


def buscar_blog(request):
    if request.POST:
        categorias = Categoria.objects.all()
        context = {
            "blogs": blog,
            "categorias": categorias,
            "cats": categorias,
            'blogs': Blogs.objects.filter(titulo__icontains=request.POST['parametro']) or Blogs.objects.filter(
                articulo__icontains=request.POST['parametro']),
            "contacto_empresa": Contacto_empresa.objects.get(),
            'contacto_redes': Contacto_redes.objects.get(),
        }
        return render_to_response("demo-digital-blog-medium-image.html", context)
    else:
        return HttpResponseRedirect("/blog/?page=1")


def contacto(request):
    contacto_empresa = Contacto_empresa.objects.all()
    confirmacion, error = '', ''
    if request.POST:
        enviar_email(request, request.POST['asunto'], request.POST['nombre'] + '<' + request.POST['email'] + '>',
                     'info@girekstudio.com', request.POST['mensaje'])
        enviar_email(request, 'Info GirekStudio', 'GirekStudio<info@girekstudio.com>', request.POST['email'],
                     'Usted a enviado un mensaje desde la Página de GirekStudio')
        confirmacion = 'Gracias por comunicarte con nosotros, pronto serás atendido por un asesor..!!!'
        return render_to_response("demo-digital-agency-contact.html", {'confirmacion': confirmacion, 'error': error})

    return render_to_response("demo-digital-agency-contact.html",
                              {'confirmacion': confirmacion, 'error': error, 'contacto_empresa': contacto_empresa})


def error404(request):
    return render_to_response("404.html")


def enviar_email(request, asunto, from_email, to, mensaje):
    asunto = asunto
    from_email = from_email
    to = to
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>' \
                   '<img src="http://girekstudio.com/static/img/girekstudio/favi%20girek-02.png"><br>' + mensaje
    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    # print from_email
