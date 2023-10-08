from rest_framework import serializers
from .models import Unidad, Servicio, Usuario

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Unidad
        fields= "__all__"
        
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Servicio
        fields= "__all__"
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= "__all__"