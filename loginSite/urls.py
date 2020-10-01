from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='loginS'),
    #path('register/', views.CreateUser, name="register"),
    path('logout/', views.logoutUser, name='logout'),
]