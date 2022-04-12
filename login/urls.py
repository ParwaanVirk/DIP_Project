from django.urls import path
from login.views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', RegistrationView.as_view(), name = 'Regis'),
    path('login/', obtain_auth_token, name = 'login'),
    path('PasswordReset/', PasswordReset.as_view(), name = "Password reset"),
    path('UserData/', UserDataView.as_view(), name = "User data"),
    path('DeleteUsers/', DeleteUsers.as_view(), name = "Delete Usrs"),
]