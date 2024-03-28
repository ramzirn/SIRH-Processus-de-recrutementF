from django.shortcuts import render
from .forms import  *
from projetPFE import settings
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
""" 
def job_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers la même page ou une autre page après avoir ajouté l'employé
            return redirect('job_details')
    else:
        form = EmployeeForm()
    return render(request, 'job-details.html', {'form': form}) """


def job_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)  # Ne pas enregistrer temporairement dans la base de données
            # Vous pouvez effectuer d'autres opérations avec les données du formulaire ici si nécessaire
            form.save()  # Maintenant, enregistrez dans la base de données
            return redirect('job_details')  # Redirection vers la même page après avoir ajouté les données
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


""" import xmlrpc.client
from django.shortcuts import render, redirect
from .forms import EmployeeForm

def job_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Sauvegarder dans Django
            form.save()
            
            # Connexion à l'API XML-RPC Odoo
            ODOO_URL = 'http://localhost:8069'
            ODOO_DB = 'SIRH_recrutement'
            ODOO_USER = 'odoo'
            ODOO_PASS = 'odoo'
            
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ODOO_URL))
            uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASS, {})
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))
            
            # Création d'un nouvel enregistrement dans Odoo
            employee_data = form.cleaned_data
            new_employee_id = models.execute_kw(ODOO_DB, uid, ODOO_PASS,
                'candidat', 'create', [{
                    'nom': employee_data['nom'],
                    'prenom': employee_data['prenom'],

                    # Ajoutez d'autres champs selon votre modèle Odoo
                }]
            )
            
            # Rediriger vers la même page ou une autre page après avoir ajouté l'employé
            return redirect('job_details')
    else:
        form = EmployeeForm()
    return render(request, 'job-details.html', {'form': form}) """




