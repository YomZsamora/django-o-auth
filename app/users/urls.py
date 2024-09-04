from django.urls import path
from users.views import UserRegisterationView

urlpatterns = [
    path('register', UserRegisterationView.as_view(), name='user-registeration'),
]
