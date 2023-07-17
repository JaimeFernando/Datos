from datosmaestros.models import CatCategoriaCatalogo, CatDependencia, CatNivelConfidencialidad

from rest_framework import serializers

class CatCategoriaCatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatCategoriaCatalogo
        exclude =('esactivo','orden','created_at','created_by','updated_at','updated_by','deleted_at','deleted_by')

class CatDependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatDependencia
        exclude =('esactivo','created_at','created_by','updated_at','updated_by','deleted_at','deleted_by')

class CatNivelConfidencialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatNivelConfidencialidad
        exclude =('esactivo','created_at','created_by','updated_at','updated_by','deleted_at','deleted_by')