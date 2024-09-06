from users.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    """
    Serializer class for user registration.
    Attributes:
    - model (User): The User model to serialize data from.
    - fields (tuple): Fields to include in the serialization process.
    """
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        