import requests,cachecontrol
from django.conf import settings
from utils.exceptions.custom_exceptions import OAuthFailed
from google.oauth2 import id_token
import google.auth.transport.requests
from rest_framework.exceptions import AuthenticationFailed

__session = requests.session()
__cached_session = cachecontrol.CacheControl(__session)
__request = google.auth.transport.requests.Request(session=__cached_session)

def get_google_token_from_auth_code(code: str) -> dict:
    
    """
    This function exchanges an authorization code for an access token using Google OAuth2.
    Args: code (str): The authorization code obtained during the OAuth flow.
    Returns: dict: A dictionary containing the response data from the token endpoint if successful.
    Raises: OAuthFailed: Custom exception raised when an error occurs during authentication.
    """
    
    payload = {
        'code': code,
        'client_id': settings.GOOGLE_CLIENT_ID,
        'client_secret': settings.GOOGLE_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_REDIRECT_URI,
        'grant_type': settings.GOOGLE_GRANT_TYPE
    }
    
    try:
        token_url = settings.GOOGLE_TOKEN_URL
        response = requests.post(token_url, data=payload).json()
        if 'access_token' in response:
            return response
        raise OAuthFailed('An error occured while authenticating user.')
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        
def get_google_user_details(access_token: str) -> dict:
    
    """
    This function retrieves user details using a Google OAuth2 access token.
    Args: access_token (str): The access token obtained after successful authentication.
    Returns: dict: A dictionary containing the user information if retrieval is successful.
    Raises: OAuthFailed: Custom exception raised when an error occurs during authentication.
    """
    
    headers = {'Authorization': f'Bearer {access_token}'}
    
    try:
        user_info_url = settings.GOOGLE_USER_INFO_URL
        response = requests.get(user_info_url, headers=headers).json()
        if 'email' in response and response['verified_email'] == True:
            return response
        raise OAuthFailed('An error occured while fetching user details.')
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        
def verify_and_decode_id_token(id_token_str: str) -> dict:
    
    """
    Verifies and decodes the Google OAuth2 ID token to retrieve user information.
    Args: id_token_str (str): The ID token received from Google's OAuth2 response.
    Returns: dict: Decoded user information.
    """
    
    try:
        decoded_token = id_token.verify_oauth2_token(id_token_str, __request, settings.GOOGLE_CLIENT_ID)
        if decoded_token and 'email' in decoded_token and decoded_token.get('email_verified', False):
            return decoded_token
        raise AuthenticationFailed()
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
    