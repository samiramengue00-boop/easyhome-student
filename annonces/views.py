from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Annonce, DemandeAnnonce
from reservations.models import Reservation

def accueil(request):
    logements = Annonce.objects.filter(disponible=True)[:6]
    return render(request, 'annonces/accueil.html', {'logements': logements})

def liste_logements(request):
    logements = Annonce.objects.filter(disponible=True)
    
    prix_max = request.GET.get('prix_max')
    if prix_max:
        logements = logements.filter(prix__lte=prix_max)
    
    localisation = request.GET.get('localisation')
    if localisation:
        logements = logements.filter(localisation__icontains=localisation)
    
    type_logement = request.GET.get('type_logement')
    if type_logement:
        logements = logements.filter(type_logement=type_logement)
    
    return render(request, 'annonces/liste.html', {'logements': logements})

def detail_logement(request, logement_id):
    logement = Annonce.objects.get(id=logement_id)
    return render(request, 'annonces/detail.html', {'logement': logement})

@login_required
def dashboard_proprietaire(request):
    if request.user.type_utilisateur != 'proprietaire':
        return redirect('accueil')
    
    logements = Annonce.objects.filter(proprietaire=request.user)
    reservations = Reservation.objects.filter(logement__in=logements)
    
    # Indicateurs
    nb_logements = logements.count()
    nb_reservations = reservations.count()
    revenus_totaux = reservations.aggregate(total=Sum('montant_total'))['total'] or 0
    commission = int(revenus_totaux * 0.1)
    
    # Données pour le graphique (réservations par mois)
    reservations_par_mois = reservations.annotate(
        mois=TruncMonth('date_reservation')
    ).values('mois').annotate(
        total=Count('id')
    ).order_by('mois')
    
    # Préparer les labels et données pour Chart.js
    mois_labels = []
    mois_data = []
    for item in reservations_par_mois:
        if item['mois']:
            mois_labels.append(item['mois'].strftime('%b %Y'))
            mois_data.append(item['total'])
    
    context = {
        'logements': logements,
        'reservations': reservations,
        'nb_logements': nb_logements,
        'nb_reservations': nb_reservations,
        'revenus_totaux': revenus_totaux,
        'commission': commission,
        'mois_labels': mois_labels,
        'mois_data': mois_data,
    }
    
    return render(request, 'annonces/dashboard_proprietaire.html', context)

@login_required
def soumettre_annonce(request):
    if request.user.type_utilisateur != 'proprietaire':
        messages.error(request, 'Seuls les propriétaires peuvent soumettre une annonce.')
        return redirect('accueil')

    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        titre = request.POST.get('titre')
        localisation = request.POST.get('localisation')
        prix = request.POST.get('prix')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        if not all([nom, email, telephone, titre, localisation, prix, description]):
            messages.error(request, '❌ Veuillez remplir tous les champs obligatoires.')
            return render(request, 'annonces/soumettre_annonce.html')

        DemandeAnnonce.objects.create(
            nom=nom,
            email=email,
            telephone=telephone,
            titre=titre,
            localisation=localisation,
            prix=int(prix),
            description=description,
            photo=photo,
            proprietaire=request.user,
            statut='en_attente'
        )

        messages.success(
            request,
            '✅ Votre demande a été soumise ! Notre équipe la traitera sous 24h.'
        )
        return redirect('dashboard_proprietaire')

    return render(request, 'annonces/soumettre_annonce.html')

@login_required
def mes_demandes(request):
    if request.user.type_utilisateur != 'proprietaire':
        return redirect('accueil')
    demandes = DemandeAnnonce.objects.filter(proprietaire=request.user)
    return render(request, 'annonces/mes_demandes.html', {'demandes': demandes})