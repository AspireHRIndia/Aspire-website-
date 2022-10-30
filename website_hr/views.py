from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        
    }
    return render(request, 'about.html', context)

def blogDetails(request):
    context = {
        
    }
    return render(request, 'blog-details.html', context)

def blog(request):
    context = {
        
    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        
    }
    return render(request, 'contact.html', context)

def portDetails(request):
    context = {
        
    }
    return render(request, 'portfolio-details.html', context)

def portfolio(request):
    context = {
        
    }
    return render(request, 'portfolio.html', context)

def services(request):
    context = {
        
    }
    return render(request, 'services.html', context)

def team(request):
    context = {
        
    }
    return render(request, 'team.html', context)