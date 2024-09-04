from rest_framework import generics
from users.serializers import UserRegistrationSerializer

class UserRegisterationView(generics.CreateAPIView):
    
    """
    API view for user registration.
    Accepts POST requests with user data to create a new user.
    """
    
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        
        """
        Custom method to set and save the user's password securely during creation.
        """
        
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        