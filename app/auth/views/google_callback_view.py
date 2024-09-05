from rest_framework import generics
from rest_framework.response import Response

from utils.exceptions.custom_exceptions import DoesNotExist
from utils.google import get_google_token_from_auth_code, verify_and_decode_id_token

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
            raise DoesNotExist("Authorization code not found")

        token_info = get_google_token_from_auth_code(code)
        id_token_str = token_info.get('id_token')
        user_info = verify_and_decode_id_token(id_token_str)

        return Response(user_info)