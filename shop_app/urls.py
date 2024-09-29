from django.urls import path 
from . import views

urlpatterns= [
    path('',views.initial, name="initial"),
    path('home',views.home, name="home"),
    path('register',views.register, name="register"),
]