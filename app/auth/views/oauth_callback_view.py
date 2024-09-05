from utils.google import get_google_token_from_auth_code

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class OAuth2CallbackView(generics.GenericAPIView):
    
    """
    API view for handling OAuth2 callback from Google.
    On receiving a GET request, it retrieves an authorization code,
    exchanges it for an access token, and fetches user information.
    """
    
    def get(self, request, *args, **kwargs):
        
        """
        Handles the GET request for OAuth2 callback.
        Retrieves authorization code, exchanges it for an access token,
        and fetches user information using the token.
        """
        
        code = request.GET.get('code')
        if not code:
            raise AuthenticationFailed()

        token_info = get_google_token_from_auth_code(code)
        return Response(token_info)
    