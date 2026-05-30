from django.urls import path
from . import views

urlpatterns = [
    path('reserver/<int:logement_id>/', views.reserver, name='reserver'),
    path('mes-reservations/', views.mes_reservations, name='mes_reservations'),
    path('contrat/<int:reservation_id>/', views.telecharger_contrat, name='telecharger_contrat'),
    path('changer-statut/<int:reservation_id>/<str:statut>/', views.changer_statut, name='changer_statut'),
]