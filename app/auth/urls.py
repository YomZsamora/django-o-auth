from django.urls import path
from auth.views import OAuth2CallbackView

urlpatterns = [
    path('oauth2callback', OAuth2CallbackView.as_view(), name='oauth-callback'),
]