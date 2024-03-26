from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def login(request):
    return render(request, 'login.html')





def about(request):
    return render(request, 'about.html')

def accueil(request):
    return render(request, 'accueil.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def index(request):
    return render(request, 'index.html')

def job_details(request):
    return render(request, 'job-details.html')

def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

def jobs(request):
    return render(request, 'jobs.html')
