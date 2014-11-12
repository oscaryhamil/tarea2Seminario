from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', inicio),
    url(r'^registrar/$',producto),
    url(r'^pedidos/$',pedido),
)