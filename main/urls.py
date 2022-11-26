from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('flutter-login-user/', flutter_login_user, name='flutter-login-user'),
    path('flutter-register-user', flutter_register_user, name='flutter-register-user'),
    path('flutter-logout-user', flutter_logout_user, name='flutter-logout-user'),
]
