from django.shortcuts import render , redirect
from .forms import  *
from projetPFE import settings
from .models import Recrutement , HRJob ,Description
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


""" def job_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=False)  # Ne pas enregistrer temporairement dans la base de données
            # Vous pouvez effectuer d'autres opérations avec les données du formulaire ici si nécessaire
            form.save()  # Maintenant, enregistrez dans la base de données
            return redirect('index')  # Redirection vers la même page après avoir ajouté les données
    else:
        form = EmployeeForm()
    return render(request, 'job-details.html', {'form': form}) """



def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

""" def jobs(request):
    return render(request, 'jobs.html')
 """

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




from django.shortcuts import render
from .models import Annonce

def jobs(request):
    annonces = Annonce.objects.all()  # Récupère toutes les annonces depuis la base de données
    return render(request, 'jobs.html', {'annonces': annonces})

def job_details(request , id):
    recrutement = Recrutement.objects.get(annonce_id=id)
    desc_id= recrutement.desc_id
    description = Description.objects.get(id=desc_id)
    tt=recrutement.intitule
    intitule=HRJob.objects.get(id=tt)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Utilisez form.cleaned_data pour obtenir les données nettoyées
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            lieu_naissance = form.cleaned_data['lieu_naissance']
            situation_familiale = form.cleaned_data['situation_familiale']
            date_naissance = form.cleaned_data['date_naissance']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            telephone = form.cleaned_data['telephone']
            adresse = form.cleaned_data['adresse']
            specialite = form.cleaned_data['specialite']
            diplome_id = form.cleaned_data['diplome_id']

            # Créez une instance de l'objet Employee avec les données récupérées
            employee = Employee.objects.create(
                nom=nom,
                prenom=prenom,
                lieu_naissance=lieu_naissance,
                situation_familiale=situation_familiale,
                date_naissance=date_naissance,
                email=email,
                mobile=mobile,
                telephone=telephone,
                adresse=adresse,
                specialite=specialite,
                diplome_id=diplome_id
            )

            # Redirigez l'utilisateur vers la page d'accueil ou une autre vue après avoir ajouté les données
            return redirect('index')
    else:
        form = EmployeeForm()

    return render(request, 'job-details.html', {'form': form , 'recrut': recrutement , 'intitule' : intitule ,'description' : description})