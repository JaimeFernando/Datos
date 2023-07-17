from rest_framework import viewsets
from rest_framework.response import Response


from datosmaestros.api.serializers.general_serializers  import CatCategoriaCatalogoSerializer,CatDependenciaSerializer,CatNivelConfidencialidadSerializer

class CatCategoriaCatalogoViewSet(viewsets.GenericViewSet):
    serializer_class = CatCategoriaCatalogoSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(esactivo = True)
    
    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
        

class CatDependenciaViewSet(viewsets.GenericViewSet):
    serializer_class = CatDependenciaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(esactivo = True)
    
    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
    
class CatNivelConfidencialidadViewSet(viewsets.GenericViewSet):
    serializer_class = CatNivelConfidencialidadSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(esactivo = True)
    
    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

