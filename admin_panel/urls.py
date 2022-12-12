from django.urls import path

from admin_panel import views

urlpatterns = [
    path('', views.adminHome, name='admin_home'),
    
]
