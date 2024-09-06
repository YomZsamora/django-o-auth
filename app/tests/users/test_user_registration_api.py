import json
from rest_framework import status
from users.models import User
from tests.abstract_api_test import AbstractAPITest
from django.urls import path, include, reverse

class UserRegistrationAPITest(AbstractAPITest):
    
    urlpatterns = [
        path('v1/user/', include('users.urls'))
    ]
    
    def setUp(self) -> None:
        super().setUp()
        self.payload = {
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "password": "@MyPassword!"
        }
        
    def test_user_can_successfully_register_a_new_account(self):
        
        response = self.client.post(reverse("user-registeration"), json.dumps( self.payload), content_type="application/json")
        print(response)
        assert response.status_code == status.HTTP_201_CREATED
        
        response_data = response.data
        registered_user = User.objects.get(email=response_data["email"])
        
        assert response_data['email'] == registered_user.email
        assert response_data['first_name'] == registered_user.first_name
        assert response_data['last_name'] == registered_user.last_name
        assert response_data['password'] == registered_user.password