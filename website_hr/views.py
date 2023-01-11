from django.shortcuts import get_object_or_404, render
from admin_panel.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'nbar': 'home'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'nbar': 'about'
    }
    return render(request, 'about.html', context)

def blogDetails(request):
    context = {
        'nbar': 'blogDetails'
    }
    return render(request, 'blog-details.html', context)

def blog(request):
    context = {
        'nbar': 'blog'
    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        'nbar': 'contact'
    }
    return render(request, 'contact.html', context)

def portDetails(request):
    context = {
        'nbar': 'portDetails'
    }
    return render(request, 'portfolio-details.html', context)

def portfolio(request):
    context = {
        'nbar': 'port'
    }
    return render(request, 'portfolio.html', context)

def services(request):
    services = Services.objects.all()
    context = {
        'services' : services,
        'nbar': 'services'
    }
    return render(request, 'services.html', context)

def jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'nbar': 'jobs'
    }
    return render(request, 'jobs.html', context)


def jobDetail(request, job_id=None):
    job = get_object_or_404(Job, job_id=job_id)
    print(job)

    context = {
        'job': job,
    }
    return render(request, 'jobDetails.html', context)

def jobDetail2(request, job_id=None):
    job = get_object_or_404(Job, job_id=job_id)
    print(job)

    context = {
        'job': job,
    }
    return render(request, 'jobDetails2.html', context)


def team(request):
    context = {
        'nbar': 'team'
    }
    return render(request, 'team.html', context)