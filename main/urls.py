from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.acceuil, name='acceuil'),
    path('app/', views.App, name='app'),
    path('auth/', views.auth, name='auth'),
    
]
