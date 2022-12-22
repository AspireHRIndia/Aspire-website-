from django.urls import path

from authapp import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    
]
