from users.models import User
from utils.exceptions.custom_exceptions import DoesNotExist

def get_user_by_email(email: str) -> User:
    
    try:
        return User.objects.get(email=email)
    except (User.DoesNotExist):
        raise DoesNotExist("The requested 'User' could not be found.")
    