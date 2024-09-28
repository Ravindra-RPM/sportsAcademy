from django.contrib import admin
from django.urls import path
from sportapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [    
    path('',views.home),
    path('index',views.home),
    path('register',views.register), 
    path('logout',views.user_logout),  
    path('dashboard',views.dashboard),   
    path('coach_list',views.coach_list),   
    path('edit_player/<playerid>',views.edit_player),   
    path('delete_player/<playerid>',views.delete_player),   
    path('create_player',views.create_player),                                       
]
