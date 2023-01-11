from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog-details/', views.blogDetails, name='blogDetails'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('portfolio-details/', views.portDetails, name='portDetails'),
    path('portfolio/', views.portfolio, name='port'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobDetail/', views.jobDetail, name='jobDetails'),
    path('jobDetail/job_id=<int:job_id>/', views.jobDetail, name='jobDetails'),
    path('jobDetail2/', views.jobDetail2, name='jobDetails2'),
    path('jobDetail2/job_id=<int:job_id>/', views.jobDetail2, name='jobDetails2'),
    
]
