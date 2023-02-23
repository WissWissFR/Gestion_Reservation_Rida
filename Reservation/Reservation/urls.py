"""Reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from reserv import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ConnexionView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('reservation', views.ReservationView.as_view()),
    path('ecole', views.EcoleView.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    
    # path('connexion/', views.connexion_view, name='connexion'),
    # path('inscription/', views.inscription_view, name='inscription'),
    # path('reservation/', views.reservation_view, name='reservation'),
    # path('ecole/', views.ecole_view, name='ecole'),
    # path('annuler/<int:reservation_id>/', views.annuler_view, name='annuler'),
    # path('deconnexion/', views.deconnexion_view, name='deconnexion'),
]