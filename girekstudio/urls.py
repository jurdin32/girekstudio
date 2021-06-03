"""girekstudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.urls import path
from django.conf.urls import *
from Inicio.views import *

urlpatterns = [
path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', index),
    path('estudio/', estudio),
    path('servicios/', servicios),
    path('portafolio/', portafolio),
    path('servicios/<int:n>/', serviciosdescripcion),
    path('portafolio/<int:n>/', portafolioimagen),
    path('tienda/', tienda),
    path('tienda/<int:id>/', producto_cate),
    path('producto/<int:n>/', producto_id),
    path('blog/', blog),
    path('blog/categoria/<int:n>/', blogfiltradocategoria),
    path('post/<int:n>/', post),
    path('post/<int:n>/<int:idBlogs>/', postrespuesta),
    path('contacto/', contacto),
    path('error/', error404),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
