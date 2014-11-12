from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
def inicio(request):
	return render_to_response('base.html',{},RequestContext(request))
def producto(request):
	if request.method=="POST":
		formu=ProductForm(request.POST)
		if(formu.is_valid()):
			formu.save()
			return HttpResponseRedirect("/")
	formu=ProductForm()
	return render_to_response("producto/registrar.html",{"formu":formu},RequestContext(request))

def pedido(request):
	if request.method=="POST":
		form=PedidoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/")
	form=PedidoForm()
	return render_to_response("producto/pedido.html",{"form":form},RequestContext(request))