from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/', views.artist, name='artist'),
    path('say-hello/', views.hello_world),
]