from django.db import models

# Create your models here.
class producto(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=500)
	precio=models.FloatField(default=0)
	stock=models.IntegerField(default=0)
	def __unicode__(self):
		return "->%s"%(self.nombre)

class pedido(models.Model):
	cliente=models.CharField(max_length=100)
	fecha_compra=models.DateField(auto_now=True)
	producto=models.ManyToManyField(producto)
	def __unicode__(self):
		return "->%s"%(self.cliente)
