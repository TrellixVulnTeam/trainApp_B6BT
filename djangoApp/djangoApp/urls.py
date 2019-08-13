"""djangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Handles all routes after and including '/' home route
    # All routes for / and e.g. /home are in train/urls
    # Django best practices?
    # When someone goes to the / (home) route Django will get rid of '/' and go to train/urls
    # Where it will find a route that matches the string that proceeds the '/'
    # E.g. /home -> train/urls finds and returns home route
    path('', include('train.urls')),
]
