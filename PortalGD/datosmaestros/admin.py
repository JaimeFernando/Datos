from django.contrib import admin
from datosmaestros.models import *

# Register your models here.
class CatCatalogoAdmin (admin.ModelAdmin):
    list_display = ('idcatalogo', 'nombre')

class CatCategoriaCatalogoAdmin (admin.ModelAdmin):
    list_display = ('idcategoriacatalogo', 'nombre')

class CatDependenciaAdmin (admin.ModelAdmin):
    list_display = ('iddependencia', 'nombre')

class CatNivelConfidencialidadAdmin (admin.ModelAdmin):
    list_display = ('idnivelconfidencialidad', 'nivelconfidencialidad')

admin.site.register(CatCatalogo, CatCatalogoAdmin)
admin.site.register(CatCategoriaCatalogo, CatCategoriaCatalogoAdmin)
admin.site.register(CatDependencia, CatDependenciaAdmin)
admin.site.register(CatNivelConfidencialidad, CatNivelConfidencialidadAdmin)