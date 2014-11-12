from django import forms
from django.forms import ModelForm
from .models import *
class ProductForm(ModelForm):
	class Meta:
		model=producto
		exclude=["usuario"]
class PedidoForm(ModelForm):
	class Meta:
		model=pedido 
		exclude=["usuario"]