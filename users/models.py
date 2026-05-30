from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    TYPE_UTILISATEUR = (
        ('etudiant', 'Étudiant'),
        ('proprietaire', 'Propriétaire'),
    )
    
    type_utilisateur = models.CharField(max_length=20, choices=TYPE_UTILISATEUR)
    telephone = models.CharField(max_length=15, blank=True)
    adresse = models.TextField(blank=True)

    code_2fa = models.CharField(max_length=6, blank=True, null=True)
    code_2fa_expiration = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_type_utilisateur_display()})"