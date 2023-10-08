from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"unidades",views.UnidadViewSet)
router.register(r"usuarios",views.UsuarioViewSet)
router.register(r"servicios",views.ServicioViewSet)
urlpatterns = [
    #path("",views.index,name="index"),
    path("",include(router.urls)),
    path("unidad/cantidad",views.unidad_count,name="unidades_count"),
]
