from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.login, name='login'),
    # Ajoutez d'autres URL si nécessaire
]
