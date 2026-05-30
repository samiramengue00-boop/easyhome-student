from django.db import models
from django.conf import settings
from annonces.models import Annonce

class Reservation(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    )
    
    etudiant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logement = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    montant_total = models.IntegerField(null=True, blank=True)
    date_reservation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.etudiant.username} - {self.logement.titre}"