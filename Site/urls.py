from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Site-Home'),
    path('Guides/', views.Guides, name='Site-Guides'),
    path('Scripts/', views.Scripts, name='Site-Scripts'),
    path('test/', views.test, name='Site-test'),
]