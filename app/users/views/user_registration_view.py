from rest_framework import generics, status
from rest_framework.response import Response

from utils.views import ApiResponse

from users.serializers import UserRegistrationSerializer

class UserRegisterationView(generics.CreateAPIView):
    
    """
    API view for user registration.
    Accepts POST requests with user data to create a new user.
    """
    
    serializer_class = UserRegistrationSerializer
    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        api_response = ApiResponse()
        api_response.code = status.HTTP_201_CREATED
        api_response.message = f"{serializer.instance.email} has been registered successfully."
        api_response.data = {
            "id": serializer.instance.id,
            "email": serializer.instance.email,
            "first_name": serializer.instance.first_name,
            "last_name": serializer.instance.last_name
        }

        return Response(vars(api_response), api_response.code)

    def perform_create(self, serializer):
        
        """
        Custom method to set and save the user's password securely during creation.
        """
        
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        