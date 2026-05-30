from django.db import models
from django.conf import settings

class Annonce(models.Model):
    TYPE_LOGEMENT = [
        ('studio', 'Studio'),
        ('chambre', 'Chambre'),
        ('appartement', 'Appartement'),
        ('villa', 'Villa'),
    ]
    
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.IntegerField()
    localisation = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='annonces/', blank=True, null=True)
    surface = models.IntegerField(null=True, blank=True)
    nombre_pieces = models.IntegerField(null=True, blank=True)
    type_logement = models.CharField(max_length=20, choices=TYPE_LOGEMENT, default='studio')
    
    def __str__(self):
        return self.titre

class PhotoLogement(models.Model):
    logement = models.ForeignKey(Annonce, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='logements/photos/')
    titre = models.CharField(max_length=100, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Photo de {self.logement.titre}"

class DemandeAnnonce(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('validee', 'Validée'),
        ('refusee', 'Refusée'),
    ]

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    titre = models.CharField(max_length=200)
    localisation = models.CharField(max_length=100)
    prix = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='demandes/', blank=True, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_soumission = models.DateTimeField(auto_now_add=True)
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.titre} — {self.nom} ({self.statut})"

    class Meta:
        verbose_name = "Demande d'annonce"
        verbose_name_plural = "Demandes d'annonces"
        ordering = ['-date_soumission']