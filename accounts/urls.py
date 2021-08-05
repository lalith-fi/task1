from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('',csrf_exempt(login_view),name="login"),
    
    path('register',csrf_exempt(register_view),name="register"),
    path('logout',csrf_exempt(logout_view),name="logout"),
    
    
]