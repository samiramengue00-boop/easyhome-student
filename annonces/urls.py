from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('logements/', views.liste_logements, name='liste_logements'),
    path('logements/<int:logement_id>/', views.detail_logement, name='detail_logement'),
    path('logements/dashboard/', views.dashboard_proprietaire, name='dashboard_proprietaire'),
    path('logements/soumettre-annonce/', views.soumettre_annonce, name='soumettre_annonce'),
    path('logements/mes-demandes/', views.mes_demandes, name='mes_demandes'),
]