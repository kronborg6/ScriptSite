from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeOnlineScripts, name='HOS'),
]