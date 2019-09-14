from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('registerProfile/', views.registerProfile, name='registerProfile'),
    path('registerStats/', views.registerStats, name='registerStats'),
    path('profile/', views.profile, name='profile'),

    # Practice URLS
    path('registerPrac/', views.registerPrac, name='registerPrac'),
    path('practice/', views.practice, name='practice'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)