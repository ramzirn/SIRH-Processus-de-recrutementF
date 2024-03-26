from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('accueil/', views.index, name='index'),
    path('job-details/', views.job_details, name='job_details'),
    path('team/', views.team, name='team'),
    path('terms/', views.terms, name='terms'),
    path('jobs/', views.jobs, name='jobs'),
]
