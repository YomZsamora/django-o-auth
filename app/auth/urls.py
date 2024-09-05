from django.urls import path
from auth.views import OAuth2CallbackView, OAuthLoginView

urlpatterns = [
    path('oauth2callback', OAuth2CallbackView.as_view(), name='oauth-callback'),
    path("oauth-login", OAuthLoginView.as_view(), name="oauth-login"),
]