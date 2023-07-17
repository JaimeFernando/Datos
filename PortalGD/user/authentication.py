from datetime import timedelta
from django.utils import timezone

from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False

    #Calcula el tiempo de Expiracion del Token, dicho tiempo se marca en una variable en el archivo settings
    def expires_in (self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds= settings.TOKEN_EXPIRED_AFTER_SECONS) - time_elapsed
        return left_time

    #Compara si el Token ya ah expirado
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)

    #Obtiene el valor si ya ha expirado el Token
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user = token.user
            #token.delete()
            token = self.get_model().objects.create(user = token.user)

        return is_expire,token

    def authenticate_credentials(self, key):
        message,token,user = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token Inválido.'
            self.expired = True
        
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado.'
        
        if token is not None:
            is_expired = self.token_expire_handler(token)
            if is_expired:
                message = 'Su Token ha expirado.'

        return (user,token,message,self.expired)