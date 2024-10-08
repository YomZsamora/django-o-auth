from utils.views import ApiResponse
from utils.google import verify_and_decode_id_token

from users.helpers import get_user_by_email

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class OAuthLoginView(APIView):
    
    """
    API view for handling OAuth login requests.
    """
    
    def post(self, request: Request) -> Response:
        
        """
        Handle POST requests to authenticate users via OAuth.
        Args: request (Request): HTTP request object containing user data.
        Returns: Response: HTTP response object with authentication status.
        Raises: AuthenticationFailed: If the ID token is missing or invalid.
        """
        
        id_token_str = request.data['id_token']
        if not id_token_str:
            raise AuthenticationFailed()
        
        token_info = verify_and_decode_id_token(id_token_str)
        user_email = token_info.get('email')
        user = get_user_by_email(user_email)
        user.refresh_last_login()
        
        # Now that we've implemented the OAuth callback view (to handle the authorization code)
        # that exchanges the authorization code for an access token and retrieves user information 
        # using the ID token, this view verifies the id token and checks if user is registered in the 
        # system using the retrieved information.
        
        api_response = ApiResponse()
        api_response.message = "Logged in successfully."
        api_response.data = token_info
        
        return Response(vars(api_response))
        