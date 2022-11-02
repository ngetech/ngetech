from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
