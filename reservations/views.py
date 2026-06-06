from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings  # ← ajout
from xhtml2pdf import pisa
from io import BytesIO
from annonces.models import Annonce
from .models import Reservation
from datetime import datetime

@login_required
def reserver(request, logement_id):
    logement = get_object_or_404(Annonce, id=logement_id)

    if request.user.type_utilisateur != 'etudiant':
        messages.error(request, 'Seuls les étudiants peuvent réserver.')
        return redirect('detail_logement', logement_id=logement_id)

    if request.method == 'POST':
        date_debut = request.POST.get('date_debut', '').strip()
        date_fin = request.POST.get('date_fin', '').strip()

        # Validation basique
        if not date_debut or not date_fin:
            messages.error(request, 'Veuillez remplir les deux dates.')
            return render(request, 'reservations/reserver.html', {'logement': logement})

        try:
            debut = datetime.strptime(date_debut, '%Y-%m-%d')
            fin = datetime.strptime(date_fin, '%Y-%m-%d')
        except ValueError:
            messages.error(request, 'Format de date invalide.')
            return render(request, 'reservations/reserver.html', {'logement': logement})

        if fin <= debut:
            messages.error(request, 'La date de départ doit être après la date d\'arrivée.')
            return render(request, 'reservations/reserver.html', {'logement': logement})

        jours = (fin - debut).days
        mois = jours / 30.44
        montant_total = int(round(mois * logement.prix))

        reservation = Reservation.objects.create(
            etudiant=request.user,
            logement=logement,
            date_debut=date_debut,
            date_fin=date_fin,
            statut='en_attente',
            montant_total=montant_total
        )

        # Email à l'étudiant — from_email = ton vrai compte Gmail ← correction clé
        try:
            send_mail(
                subject='Réservation confirmée - EasyHome Student',
                message=(
                    f'Bonjour {request.user.username},\n\n'
                    f'Votre réservation a été enregistrée !\n\n'
                    f'Logement : {logement.titre}\n'
                    f'Localisation : {logement.localisation}\n'
                    f'Dates : du {date_debut} au {date_fin}\n'
                    f'Montant total : {montant_total} FCFA\n\n'
                    f'Téléchargez votre contrat depuis "Mes réservations".\n\n'
                    f'L\'équipe EasyHome'
                ),
                from_email=settings.EMAIL_HOST_USER,  # ← correction : plus de noreply@easyhome.sn
                recipient_list=[request.user.email],
                fail_silently=True,
            )
        except Exception:
            pass

        # Email au propriétaire
        if logement.proprietaire and logement.proprietaire.email:
            try:
                send_mail(
                    subject='Nouvelle réservation - EasyHome Student',
                    message=(
                        f'Bonjour {logement.proprietaire.username},\n\n'
                        f'Un étudiant a réservé votre logement "{logement.titre}".\n\n'
                        f'Dates : du {date_debut} au {date_fin}\n'
                        f'Montant total : {montant_total} FCFA\n\n'
                        f'Connectez-vous à votre tableau de bord pour gérer cette réservation.\n\n'
                        f'L\'équipe EasyHome'
                    ),
                    from_email=settings.EMAIL_HOST_USER,  # ← correction ici aussi
                    recipient_list=[logement.proprietaire.email],
                    fail_silently=True,
                )
            except Exception:
                pass

        messages.success(request, f'Réservation confirmée ! Total : {montant_total} FCFA')
        return redirect('mes_reservations')

    return render(request, 'reservations/reserver.html', {'logement': logement})


@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(
        etudiant=request.user
    ).select_related('logement').order_by('-id')
    return render(request, 'reservations/mes_reservations.html', {'reservations': reservations})


@login_required
def telecharger_contrat(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, etudiant=request.user)
    context = {
        'reservation': reservation,
        'etudiant': reservation.etudiant,
        'logement': reservation.logement,
        'date_aujourdhui': datetime.now().strftime('%d/%m/%Y'),
    }
    html_string = render_to_string('reservations/contrat.html', context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="contrat_{reservation.id}.pdf"'
        return response
    return HttpResponse('Erreur lors de la génération du PDF', status=400)


@login_required
def changer_statut(request, reservation_id, statut):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.user == reservation.logement.proprietaire:
        if statut in ['confirmee', 'annulee']:
            reservation.statut = statut
            reservation.save()
            messages.success(request, f'Réservation {statut} avec succès.')
    return redirect('dashboard_proprietaire')