from users.models import User
from utils.exceptions.custom_exceptions import DoesNotExist

def get_user_by_email(email: str) -> User:
    
    """
    Retrieve a User object based on the provided email address.
    Parameters: email (str): The email address of the user to retrieve.
    Returns: User: The User object associated with the provided email address.
    Raises: DoesNotExist: Custom exception raised when the user with the given email does not exist in the database.
    """
    
    try:
        return User.objects.get(email=email)
    except (User.DoesNotExist):
        raise DoesNotExist(f"{email} could not be found.")
    