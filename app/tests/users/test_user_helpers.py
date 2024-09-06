import pytest
from users.helpers import get_user_by_email
from tests.abstract_api_test import AbstractAPITest
from utils.exceptions.custom_exceptions import DoesNotExist

class UserHelpersTest(AbstractAPITest):
    
    urlpatterns = []
    
    def setUp(self) -> None:
        super().setUp()
        self.seed_registered_user()
        
    def test_get_user_by_email_successful(self):
        
        retrieved_user = get_user_by_email(self.registered_user.email)
        
        assert retrieved_user.id == self.registered_user.id
        assert retrieved_user.email == self.registered_user.email
        assert retrieved_user.first_name == self.registered_user.first_name
        assert retrieved_user.last_name == self.registered_user.last_name
        
    def test_get_user_by_email_raises_404_exception_for_non_existing_emails(self):
        
        non_existent_email = "nonexistent@example.com"
        with pytest.raises(DoesNotExist) as exc_info:
            get_user_by_email(non_existent_email)
        assert f"{non_existent_email} could not be found." in str(exc_info.value)
        