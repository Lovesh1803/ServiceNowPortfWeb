from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('services/', views.services_page, name='services'),
    path('login/', views.sign_in, name='sign_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signout/', views.sign_out, name='sign_out'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
]
