"""
URL configuration for SmileSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('signin.html',views.signin, name='signin'),
    path('signup.html',views.signup, name='signup'),
    path('service.html',views.service, name='service'),
    path('blog.html',views.blog, name='blog'),
    path('contactus.html',views.contactus, name='contactus'),
    path('location.html',views.location, name='location'),
    path('forgot.html',views.forgot, name='forgot')
]






