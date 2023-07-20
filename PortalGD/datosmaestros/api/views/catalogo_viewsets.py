from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


from user.authentication_mixins import Authentication

from datosmaestros.api.serializers.catalogo_serializer import CatCatalogoSerializer

class CatCatalogoViewSet(viewsets.ModelViewSet):
    
    serializer_class = CatCatalogoSerializer
    
    #Utilizando el Metodo Get podemos listar los Registros
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(idcatalogo = pk, is_active = True).first()

    #Aqui se esta sobre escribiendo la funcion, mas no es necesario, esto lo hacemos para que podamos manipular las respuestas y mensajes de cada metodo
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'message':'Catalogo creado correctamente!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
    
    #Mandamos la informacion por metodo PUT para poder actualizar el registro
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            catalogo_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if catalogo_serializer.is_valid():
                catalogo_serializer.save()
                return Response(catalogo_serializer.data,status = status.HTTP_200_OK)
            return Response(catalogo_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    #Acemos una consulta para ver si existe el registro mediante su ID y procedemos a borrarlo, indicnado que se actualizara a flaso en la columna esactivo
    def destroy(self,request,pk=None):
        catalogo = self.get_queryset().filter(idcatalogo = pk).first()
        if catalogo:
            catalogo.is_active = False
            catalogo.save()
            return Response({'message':'Catalogo Borrado correctamente!'},status=status.HTTP_200_OK)
        return Response({'error':'No existe un Catalogo con esos datos'},status=status.HTTP_400_BAD_REQUEST)
