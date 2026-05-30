from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.modifier_profil, name='modifier_profil'),
    path('profil/', views.modifier_profil, name='modifier_profil'),
    path('verifier-code/', views.verifier_code, name='verifier_code'),
]