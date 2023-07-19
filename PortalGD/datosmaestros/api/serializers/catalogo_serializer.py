from rest_framework import serializers
from datosmaestros.models import CatCatalogo

class CatCatalogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatCatalogo
        exclude =('updated_by','deleted_at','deleted_by')

    def to_representation(self, instance):
        return {
            'idcatalogo':instance.idcatalogo,
            'nombre':instance.nombre,
            'descripcion':instance.descripcion,
            'iddependencia': instance.iddependencia.nombre,
            'idcategoriacatalogo': instance.idcategoriacatalogo.nombre,
            'idnivelconfidencialidad': instance.idnivelconfidencialidad.nivelconfidencialidad,
            'areaatribucion':instance.areaatribucion,
            'fundamentojuridico':instance.fundamentojuridico,
            'tabledata':instance.tabledata,
            'pathinstructivo':instance.pathinstructivo,
            'apidata':instance.apidata,
            'pathinstructivoapidata':instance.pathinstructivoapidata,
            'orden': instance.orden,
            'nombrecustodio':instance.nombrecustodio,
            'puestocustodio':instance.puestocustodio,
            'nombreduenio':instance.nombreduenio,
            'puestoduenio':instance.puestoduenio,
            'is_active': instance.is_active,
            'updated_at': instance.updated_at,
        }