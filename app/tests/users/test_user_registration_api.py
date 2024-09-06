import json
from rest_framework import status
from users.models import User
from users.serializers import UserRegistrationSerializer
from tests.abstract_api_test import AbstractAPITest
from django.urls import path, include, reverse

class UserRegistrationAPITest(AbstractAPITest):
    
    urlpatterns = [
        path('v1/user/', include('users.urls'))
    ]
    
    def setUp(self) -> None:
        super().setUp()
        self.user_email = self.fake.email()
        self.payload = {
            "email": self.user_email,
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "password": "@MyPassword!"
        }
        
    def test_user_registration_successful(self):
        
        response = self.client.post(reverse("user-registeration"), json.dumps( self.payload), content_type="application/json")
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['status'] == "success"
        assert response.data['message'] == f"{self.user_email} has been registered successfully."
        
        response_data = response.data['data']
        registered_user = User.objects.get(email=response_data["email"])
        
        assert str(registered_user) == self.user_email
        
        assert response_data['id'] == registered_user.id      
        assert response_data['email'] == registered_user.email
        assert response_data['first_name'] == registered_user.first_name
        assert response_data['last_name'] == registered_user.last_name

    def test_required_fields_exception_raised(self):
        
        self.payload = {}
        serializer = UserRegistrationSerializer(data=self.payload)
        is_valid = serializer.is_valid()
        errors = serializer.errors
        
        assert not is_valid
        assert errors['email'][0] == "This field is required."
        assert errors['password'][0] == "This field is required."
        
    def test_existing_or_registered_email_exception_raised(self):
        
        self.seed_registered_user()
        self.payload['email'] = self.registered_user.email
        
        response = self.client.post(reverse("user-registeration"), json.dumps( self.payload), content_type="application/json")
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "user with this email already exists." in response.data['email'][0]
        