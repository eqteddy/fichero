from django.db import models
from .validators import validar_codigo,validar_login
# Create your models here.
class Unidad(models.Model):
    cod_unidad = models.CharField(max_length=10,unique=True,validators=[validar_codigo])
    nombre = models.CharField(max_length=50,unique=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
 

class Servicio(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(blank = True,default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
class Usuario(models.Model):
    login = models.CharField(max_length=20,unique=True,validators=[validar_login])
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    estado = models.BooleanField(blank=True,default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
 
class Atencion(models.Model):
    unidad = models.ForeignKey(Unidad,null=True,on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio,null=True,on_delete=models.PROTECT)
    Usuario = models.ForeignKey(Usuario,null=True,on_delete=models.PROTECT)
    numeroFicha = models.IntegerField()
     
        