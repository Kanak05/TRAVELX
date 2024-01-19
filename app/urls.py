from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.home, name = 'home'),
    path('home',views.home, name = 'home'),
    path('success',views.success, name = 'success'),
    path('signup',views.user, name = 'index'),
    path('nikhil',views.nikhil, name = 'nikhil'),
    path('goa',views.goa,name='goa'),
    path('prem',views.prem,name='prem'),
    path('sun_temple',views.sun_temple,name='sun_temple'),
    path('Dwarka',views.Dwarka,name='Dwarka'),
    path('varanasi',views.varanasi,name='varanasi'),
    # path('login',views.login,name='login'),

  
]