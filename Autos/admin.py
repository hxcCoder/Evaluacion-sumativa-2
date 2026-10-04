from django.contrib import admin
from .models import Auto

# Configuración administrativa útil para visualizar y buscar los datos
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio') # Columnas visibles en el admin
    search_fields = ('marca', 'modelo')                 # Barra de búsqueda
    list_filter = ('año',)                              # Filtro lateral

# Register your models here.
admin.site.register(Auto, AutoAdmin)