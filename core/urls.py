
from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name='core'

urlpatterns = [
   
    path('Home',views.Home,name='Home'),
    path('',views.Home,name='Home'),

    path('login',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('signup',views.signup,name='signup'),
    
] 
