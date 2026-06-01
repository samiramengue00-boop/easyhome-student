import random
import string
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Utilisateur

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        type_utilisateur = request.POST['type_utilisateur']
        telephone = request.POST['telephone']
        
        if password != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas')
            return redirect('inscription')
        
        if Utilisateur.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur existe déjà')
            return redirect('inscription')
        
        user = Utilisateur.objects.create_user(
            username=username,
            password=password,
            email=email,
            type_utilisateur=type_utilisateur,
            telephone=telephone
        )
        
        login(request, user)
        return redirect('accueil')
    
    return render(request, 'users/inscription.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.type_utilisateur == 'proprietaire':
                return redirect('dashboard_proprietaire')
            else:
                return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect')
    
    return render(request, 'users/connexion.html')


def verifier_code(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('connexion')
    
    user = get_object_or_404(Utilisateur, id=user_id)
    
    if request.method == 'POST':
        code_saisi = request.POST.get('code')
        
        if (user.code_2fa == code_saisi and 
            user.code_2fa_expiration and 
            user.code_2fa_expiration > timezone.now()):
            login(request, user)
            user.code_2fa = None
            user.code_2fa_expiration = None
            user.save()
            del request.session['user_id']
            
            if user.type_utilisateur == 'proprietaire':
                return redirect('dashboard_proprietaire')
            else:
                return redirect('accueil')
        else:
            messages.error(request, 'Code invalide ou expiré')
    
    return render(request, 'users/verifier_code.html', {'email': user.email})


def deconnexion(request):
    logout(request)
    return redirect('accueil')


@login_required
def modifier_profil(request):
    if request.method == 'POST':
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        
        request.user.email = email
        request.user.telephone = telephone
        request.user.adresse = adresse
        request.user.save()
        
        nouveau_mdp = request.POST.get('nouveau_mot_de_passe')
        if nouveau_mdp:
            request.user.set_password(nouveau_mdp)
            request.user.save()
            update_session_auth_hash(request, request.user)
        
        messages.success(request, 'Profil modifié avec succès !')
        return redirect('modifier_profil')
    
    return render(request, 'users/modifier_profil.html')