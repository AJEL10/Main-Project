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
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index2/',views.index2, name='index2'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('login/', views.patient_login, name='patient_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('appointment/', views.patient_appointment, name='patient_appointment'),
    # path('new-appointment/', views.new_appointment, name='new_appointment'),
    path('reset-password/', views.reset_password, name='reset_password'),

    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('accept-appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    path('reject-appointment/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clinic_register/', views.clinic_register, name='clinic_register'),
    path('Register_cards/', views.Register_cards, name='Register_cards'),
    path('Login_cards/', views.Login_cards, name='Login_cards'),
    path('clinic_login', views.clinic_login, name='clinic_login'),
    path('clinic_dashboard', views.clinic_dashboard, name='clinic_dashboard'),
    
    # path('admin-register/', views.admin_register, name='admin_register'),


]




