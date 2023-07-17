from datetime import datetime

from django.contrib.sessions.models import Session 

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import UserTokenSerializer

class UserToken (APIView):
    def get(self,request,*args,**kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error':'Credenciales enviadas incorrectas'
            },status = status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):

    def post(self,request,*args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                #Al Iniciar Sesion Crea el Token
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesion Exitoso'
                    }, status=status.HTTP_201_CREATED)
                #Si el usuari ya ha iniciado session y tiene token creado, busca la session actual, borra las sessiones anteriores y crea un nuevo token
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    #Aqui es donde Borra el Anterior Token y Crea uno Nuevo
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de Sesion Exitoso'
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre de Usuario o Contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
    

class Logout(APIView):

    def post(self,request,*args, **kwargs):
        try:
            #Recibimos el Token
            token = Token.objects.filter(key = request.POST.get('token')).first()
            #validamos si el Toekn pertenence a un Usuario
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                #Si pertenence a un Usuario y tiene session activa, se elimina la session y el Token
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesiones de Usuario Eliminadas.'
                token_message = 'Token Eliminado.'
                return Response({'token_message': token_message, 'session_message': session_message}, status = status.HTTP_200_OK)
            
            return Response({'error':'No se ha encontrado un usuario con estas Credenciales.'}, status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({'error':'No se ha encontrado token en la petición.'}, status=status.HTTP_409_CONFLICT)