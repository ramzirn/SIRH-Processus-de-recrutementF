from django.shortcuts import render , redirect
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
from .models import Annonce, Besoin, HRJob, RecruitmentDegree, ResourceCalendar

def jobs(request):
    annonces = Annonce.objects.all()
    
      # Récupère toutes les annonces depuis la base de données
    return render(request, 'jobs.html', {'annonces': annonces})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Besoin, HRJob
from .forms import CandidateEvaluationForm

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CandidateEvaluationForm
from .models import Besoin, HRJob

def job_details(request, id):
    besoin = get_object_or_404(Besoin, id=id)
    tt = besoin.intitule
    re=besoin.niveau
    rf=besoin.horaires
    hrjob = get_object_or_404(HRJob, id=tt)
    rc = get_object_or_404(RecruitmentDegree, id=re)
    tg = get_object_or_404(ResourceCalendar, id=rf)


    if request.method == 'POST':
        form = CandidateEvaluationForm(request.POST)
        if form.is_valid():
            # Ajouter la valeur job_id au formulaire avant de le sauvegarder
            form.instance.job_id = hrjob.id
            form.instance.department_id = hrjob.department_id
            form.save()
            return redirect('jobs')  # Remplacez par votre vue de succès
    else:
        # Créer le formulaire avec la valeur initial de job_id
        form = CandidateEvaluationForm()

    return render(request, 'job-details.html', { 
        'besoin': besoin, 
        'job': hrjob,
        'form': form,
        'lvl' : rc,
        'hr' :tg
    })
