# orders/urls.py

from django.urls import path
from .views import create_user, get_restaurants

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('restaurants/', get_restaurants, name='get_restaurants'),
]
