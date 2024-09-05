from utils.views import ApiResponse
from utils.google import verify_and_decode_id_token

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

class OAuthLoginView(APIView):
    
    def post(self, request: Request) -> Response:
        
        id_token_str = request.data['id_token']
        if not id_token_str:
            raise AuthenticationFailed()
        
        token_info = verify_and_decode_id_token(id_token_str)
        user_email = token_info.get('email')
        
        api_response = ApiResponse()
        api_response.message = "Logged in successfully."
        api_response.data = token_info
        
        return Response(vars(api_response))
        

            
        