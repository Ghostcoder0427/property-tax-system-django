# urls.py
from django.urls import path
from . import views
urlpatterns = [
     # Add this line for the index page
    path('', views.home_view, name='home_url'),
    path('register/', views.register_view, name='register_url'),
    path('login/', views.login_view, name='login_url'),
    path('contact/', views.contact_view, name='contact_url'),
    path('about/', views.about_view, name='about_url'),
  
    
]