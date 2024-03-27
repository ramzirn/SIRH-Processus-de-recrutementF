from django.shortcuts import render
from .forms import  *
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
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers la même page ou une autre page après avoir ajouté l'employé
            return redirect('job_details')
    else:
        form = EmployeeForm()
    return render(request, 'job-details.html', {'form': form})


def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

def jobs(request):
    return render(request, 'jobs.html')


def candidatForm(request):
    return render (request,'candidateForm.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirection après l'ajout d'un employé
            return redirect('index')  # Remplacez 'index' par le nom de votre vue d'accueil
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})