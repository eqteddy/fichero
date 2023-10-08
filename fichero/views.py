from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import UnidadSerializer,UsuarioSerializer,ServicioSerializer
from .models import Unidad,Servicio,Usuario,Atencion
# Create your views here.
def index(request):
    return HttpResponse("Hola")

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
@api_view(["GET"])
def unidad_count(request):
    """
    Cantidad de Unidades
    """
    try:
        cantidad = Unidad.objects.count();
        return JsonResponse(
            {"cantidad": cantidad},
            safe = False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message":str(e)},safe=False, status=500)