from rest_framework import generics
from rest_framework.response import Response

from utils.exceptions.custom_exceptions import DoesNotExist
from utils.google import get_google_token_from_auth_code, get_google_user_details

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
        
        # Retrieve the authorization code from the request parameters.
        code = request.GET.get('code')
        if not code:
            raise DoesNotExist("Authorization code not found")

        # Exchange the authorization code for an access token
        token_info = get_google_token_from_auth_code(code)
        print(token_info)
        # Extract the access token
        access_token = token_info.get('access_token')
        # Use the access token to access user info or other resources
        user_info = get_google_user_details(access_token)

        return Response(user_info)