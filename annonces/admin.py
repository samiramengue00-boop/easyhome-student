from django.contrib import admin
from .models import Annonce, PhotoLogement, DemandeAnnonce

class PhotoInline(admin.TabularInline):
    model = PhotoLogement
    extra = 3

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'localisation', 'prix', 'disponible', 'type_logement')
    list_filter = ('type_logement', 'disponible')
    search_fields = ('titre', 'localisation')
    inlines = [PhotoInline]

@admin.register(PhotoLogement)
class PhotoLogementAdmin(admin.ModelAdmin):
    list_display = ('logement', 'titre', 'date_ajout')

@admin.register(DemandeAnnonce)
class DemandeAnnonceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'nom', 'telephone', 'localisation', 'prix', 'statut', 'date_soumission']
    list_filter = ['statut', 'localisation']
    search_fields = ['nom', 'titre', 'email']
    actions = ['valider_et_publier', 'refuser_demandes']

    def valider_et_publier(self, request, queryset):
        for demande in queryset:
            if demande.statut == 'en_attente':
                Annonce.objects.create(
                    titre=demande.titre,
                    localisation=demande.localisation,
                    prix=demande.prix,
                    description=demande.description,
                    image=demande.photo,
                    proprietaire=demande.proprietaire,
                    disponible=True
                )
                demande.statut = 'validee'
                demande.save()
        self.message_user(request, f'✅ {queryset.count()} annonce(s) validée(s) et publiée(s).')
    valider_et_publier.short_description = "✅ Valider et publier"

    def refuser_demandes(self, request, queryset):
        queryset.update(statut='refusee')
        self.message_user(request, f'❌ {queryset.count()} demande(s) refusée(s).')
    refuser_demandes.short_description = "❌ Refuser les demandes"