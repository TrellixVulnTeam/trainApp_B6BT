from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

