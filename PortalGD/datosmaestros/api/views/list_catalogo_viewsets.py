from rest_framework import viewsets
from datosmaestros.models  import CatCatalogo
from datosmaestros.api.serializers.catalogo_serializer import CatCatalogoSerializer
from datosmaestros.api.serializers.general_serializers import CatCategoriaCatalogoSerializer,CatDependenciaSerializer

class CatCatalogoViewSet(viewsets.ModelViewSet):
    queryset = CatCatalogo.objects.all()
    serializer_class = CatCatalogoSerializer

    def get_serializer_class(self):
        # Obtiene el nombre de la tabla correspondiente al registro actual
        tabla = self.get_object().tableData

        # Retorna el serializador correspondiente a la tabla
        if tabla == 'catDependencia':
            return CatDependenciaSerializer
        elif tabla == 'catCategoriaCatalogo':
            return CatCategoriaCatalogoSerializer
        else:
            return CatCatalogoSerializer