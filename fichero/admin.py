from django.contrib import admin
from .models import Unidad
from .models import Usuario
from .models import Atencion
from .models import Servicio

# Register your models here.
class UnidadAdmin(admin.ModelAdmin):
    list_display = ("nombre","cod_unidad")
admin.site.register(Unidad,UnidadAdmin)
admin.site.register(Usuario)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre","estado","created")
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Atencion)