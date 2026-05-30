from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'type_utilisateur', 'telephone')
    list_filter = ('type_utilisateur',)
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {'fields': ('type_utilisateur', 'telephone', 'adresse')}),
    )

admin.site.register(Utilisateur, UtilisateurAdmin)