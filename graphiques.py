import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

# ============================================================
# GRAPHIQUE 1 — Situation de logement actuelle (Camembert)
# ============================================================
labels1 = [
    'Appartement privé',
    'Pas encore au Sénégal',
    'Chez un proche',
    'Résidence universitaire',
    'Collocation',
    'Hors Sénégal'
]
valeurs1 = [36, 14, 5, 3, 1, 1]
couleurs1 = ['#1e3c72', '#2a5298', '#4484d8', '#74b5f5', '#f5a623', '#ffd87a']
explode1 = (0.05, 0.05, 0, 0, 0, 0)

fig1, ax1 = plt.subplots(figsize=(9, 6))
wedges, texts, autotexts = ax1.pie(
    valeurs1, labels=labels1, autopct='%1.1f%%',
    colors=couleurs1, explode=explode1,
    startangle=140, textprops={'fontsize': 10}
)
for at in autotexts:
    at.set_fontweight('bold')
    at.set_color('white')
ax1.set_title(
    'Figure 1 : Situation de logement actuelle des répondants (n=60)',
    fontsize=13, fontweight='bold', pad=20
)
plt.tight_layout()
plt.savefig('figure1_situation_logement.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 1 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 2 — Âge des répondants étudiants (Barres)
# ============================================================
ages = ['Moins de 20 ans', '20 – 23 ans', '24 – 27 ans', '28 ans et plus']
valeurs2 = [8, 32, 15, 5]
pourcentages2 = ['13,3%', '53,3%', '25,0%', '8,4%']
couleurs2 = ['#74b5f5', '#1e3c72', '#2a5298', '#f5a623']

fig2, ax2 = plt.subplots(figsize=(9, 5))
barres2 = ax2.bar(ages, valeurs2, color=couleurs2,
                   width=0.5, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres2, pourcentages2):
    ax2.text(
        barre.get_x() + barre.get_width() / 2,
        barre.get_height() + 0.4,
        f'{pct}',
        ha='center', va='bottom',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax2.set_title(
    'Figure 2 : Répartition des étudiants par tranche d\'âge (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax2.set_ylabel('Nombre de répondants', fontsize=11)
ax2.set_ylim(0, 40)
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure2_ages.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 2 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 3 — Villes concernées étudiants (Barres horizontales)
# ============================================================
villes = ['Saint-Louis', 'Thiès', 'Dakar']
valeurs3 = [8, 14, 38]
pourcentages3 = ['13,3%', '23,3%', '63,3%']
couleurs3 = ['#74b5f5', '#2a5298', '#1e3c72']

fig3, ax3 = plt.subplots(figsize=(9, 4))
barres3 = ax3.barh(villes, valeurs3, color=couleurs3,
                    height=0.4, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres3, pourcentages3):
    ax3.text(
        barre.get_width() + 0.3,
        barre.get_y() + barre.get_height() / 2,
        f'{pct}',
        ha='left', va='center',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax3.set_title(
    'Figure 3 : Villes ciblées par les étudiants répondants (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax3.set_xlabel('Nombre de répondants', fontsize=11)
ax3.set_xlim(0, 46)
ax3.grid(axis='x', alpha=0.3, linestyle='--')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure3_villes_etudiants.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 3 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 4 — Budgets étudiants (Barres)
# ============================================================
labels4 = [
    'Moins de\n60 000 FCFA',
    '60 000 –\n90 000 FCFA',
    'Plus de\n100 000 FCFA'
]
valeurs4 = [11, 42, 7]
pourcentages4 = ['18,3%', '70,0%', '11,7%']
couleurs4 = ['#4484d8', '#1e3c72', '#f5a623']

fig4, ax4 = plt.subplots(figsize=(8, 5))
barres4 = ax4.bar(labels4, valeurs4, color=couleurs4,
                   width=0.5, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres4, pourcentages4):
    ax4.text(
        barre.get_x() + barre.get_width() / 2,
        barre.get_height() + 0.5,
        f'{pct}',
        ha='center', va='bottom',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax4.set_title(
    'Figure 4 : Répartition des budgets mensuels des étudiants (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax4.set_ylabel('Nombre de répondants', fontsize=11)
ax4.set_ylim(0, 50)
ax4.grid(axis='y', alpha=0.3, linestyle='--')
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure4_budgets.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 4 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 5 — Critères prioritaires étudiants (Barres horizontales)
# ============================================================
criteres = [
    'Confort\n(eau, électricité, internet)',
    'Sécurité',
    'Localisation\n(proximité université)',
    'Prix'
]
valeurs5 = [33, 44, 47, 49]
pourcentages5 = ['55,0%', '73,3%', '78,3%', '81,7%']
couleurs5 = ['#74b5f5', '#4484d8', '#2a5298', '#1e3c72']

fig5, ax5 = plt.subplots(figsize=(10, 5))
barres5 = ax5.barh(criteres, valeurs5, color=couleurs5,
                    height=0.5, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres5, pourcentages5):
    ax5.text(
        barre.get_width() + 0.5,
        barre.get_y() + barre.get_height() / 2,
        f'{pct}',
        ha='left', va='center',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax5.set_title(
    'Figure 5 : Critères de recherche prioritaires des étudiants (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax5.set_xlabel('Nombre de répondants', fontsize=11)
ax5.set_xlim(0, 58)
ax5.grid(axis='x', alpha=0.3, linestyle='--')
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure5_criteres.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 5 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 6 — Difficultés étudiants (Camembert)
# ============================================================
labels6 = [
    'Ont eu des difficultés\n(63,3%)',
    "N'ont pas eu\nde difficultés (36,7%)"
]
valeurs6 = [38, 22]
couleurs6 = ['#1e3c72', '#74b5f5']
explode6 = (0.05, 0)

fig6, ax6 = plt.subplots(figsize=(7, 5))
wedges6, texts6, autotexts6 = ax6.pie(
    valeurs6, labels=labels6, autopct='%1.1f%%',
    colors=couleurs6, explode=explode6,
    startangle=90, textprops={'fontsize': 11}
)
for at in autotexts6:
    at.set_fontweight('bold')
    at.set_color('white')
ax6.set_title(
    'Figure 6 : Difficultés rencontrées pour trouver un logement (n=60)',
    fontsize=13, fontweight='bold', pad=20
)
plt.tight_layout()
plt.savefig('figure6_difficultes.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 6 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 7 — Intérêt étudiants pour la plateforme (Barres)
# ============================================================
interet_etu = ['Oui']
valeurs7 = [60]
couleurs7 = ['#1e3c72']

fig7, ax7 = plt.subplots(figsize=(6, 5))
barres7 = ax7.bar(interet_etu, valeurs7, color=couleurs7,
                   width=0.3, edgecolor='white', linewidth=1.5)
ax7.text(
    0, 61, '100%',
    ha='center', va='bottom',
    fontweight='bold', fontsize=16, color='#1e3c72'
)
ax7.set_title(
    'Figure 7 : Intérêt des étudiants pour une plateforme numérique (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax7.set_ylabel('Nombre de répondants', fontsize=11)
ax7.set_ylim(0, 70)
ax7.grid(axis='y', alpha=0.3, linestyle='--')
ax7.spines['top'].set_visible(False)
ax7.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure7_interet_etudiants.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 7 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 8 — Fonctionnalités souhaitées étudiants (Barres)
# ============================================================
fonctionnalites = [
    'Assistance\nadministrative',
    'Avis et\névaluations',
    'Réservation\nen ligne',
    'Recherche\nprix/localisation'
]
valeurs8 = [25, 28, 34, 60]
pourcentages8 = ['41,7%', '46,7%', '56,7%', '100%']
couleurs8 = ['#74b5f5', '#4484d8', '#2a5298', '#1e3c72']

fig8, ax8 = plt.subplots(figsize=(9, 5))
barres8 = ax8.bar(fonctionnalites, valeurs8, color=couleurs8,
                   width=0.5, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres8, pourcentages8):
    ax8.text(
        barre.get_x() + barre.get_width() / 2,
        barre.get_height() + 0.5,
        f'{pct}',
        ha='center', va='bottom',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax8.set_title(
    'Figure 8 : Fonctionnalités souhaitées par les étudiants (n=60)',
    fontsize=13, fontweight='bold', pad=15
)
ax8.set_ylabel('Nombre de répondants', fontsize=11)
ax8.set_ylim(0, 70)
ax8.grid(axis='y', alpha=0.3, linestyle='--')
ax8.spines['top'].set_visible(False)
ax8.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure8_fonctionnalites.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 8 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 9 — Villes concernées propriétaires (Barres horizontales)
# ============================================================
villes_proprio = ['Saint-Louis', 'Thiès', 'Dakar']
valeurs9 = [3, 4, 13]
pourcentages9 = ['15%', '20%', '65%']
couleurs9 = ['#74b5f5', '#2a5298', '#1e3c72']

fig9, ax9 = plt.subplots(figsize=(9, 4))
barres9 = ax9.barh(villes_proprio, valeurs9, color=couleurs9,
                    height=0.4, edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres9, pourcentages9):
    ax9.text(
        barre.get_width() + 0.2,
        barre.get_y() + barre.get_height() / 2,
        f'{pct}',
        ha='left', va='center',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax9.set_title(
    'Figure 9 : Villes des propriétaires répondants (n=20)',
    fontsize=13, fontweight='bold', pad=15
)
ax9.set_xlabel('Nombre de propriétaires', fontsize=11)
ax9.set_xlim(0, 17)
ax9.grid(axis='x', alpha=0.3, linestyle='--')
ax9.spines['top'].set_visible(False)
ax9.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure9_villes_proprietaires.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 9 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 10 — Méthodes publication propriétaires (Barres horizontales)
# ============================================================
methodes = [
    'Agence\nimmobilière',
    'WhatsApp',
    'Bouche-à-\noreille',
    'Facebook'
]
valeurs10 = [5, 4, 5, 8]
pourcentages10 = ['25%', '20%', '25%', '40%']

fig10, ax10 = plt.subplots(figsize=(9, 5))
barres10 = ax10.barh(methodes, valeurs10,
                      color='#1e3c72', height=0.5,
                      edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres10, pourcentages10):
    ax10.text(
        barre.get_width() + 0.1,
        barre.get_y() + barre.get_height() / 2,
        pct, ha='left', va='center',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax10.set_title(
    'Figure 10 : Méthodes de publication des propriétaires (n=20)',
    fontsize=13, fontweight='bold', pad=15
)
ax10.set_xlabel('Nombre de propriétaires', fontsize=11)
ax10.set_xlim(0, 11)
ax10.grid(axis='x', alpha=0.3, linestyle='--')
ax10.spines['top'].set_visible(False)
ax10.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure10_methodes_publication.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 10 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 11 — Intérêt propriétaires pour EasyHome (Camembert)
# ============================================================
labels11 = [
    'Oui, certainement\n(70%)',
    'Oui, probablement\n(20%)',
    'Peut-être\n(10%)'
]
valeurs11 = [14, 4, 2]
couleurs11 = ['#1e3c72', '#4484d8', '#f5a623']

fig11, ax11 = plt.subplots(figsize=(7, 5))
wedges11, texts11, autotexts11 = ax11.pie(
    valeurs11, labels=labels11, autopct='%1.1f%%',
    colors=couleurs11, startangle=90,
    textprops={'fontsize': 10}
)
for at in autotexts11:
    at.set_fontweight('bold')
    at.set_color('white')
ax11.set_title(
    'Figure 11 : Intérêt des propriétaires pour EasyHome (n=20)',
    fontsize=13, fontweight='bold', pad=20
)
plt.tight_layout()
plt.savefig('figure11_interet_proprietaires.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 11 sauvegardée ✅")


# ============================================================
# GRAPHIQUE 12 — Modèle paiement propriétaires (Barres horizontales)
# ============================================================
paiements = [
    'Non',
    'Commission\nréservation',
    '5 000 –\n10 000 FCFA',
    'Moins de\n5 000 FCFA'
]
valeurs12 = [1, 4, 5, 9]
pourcentages12 = ['5%', '20%', '25%', '45%']
couleurs12 = ['#e74c3c', '#f5a623', '#4484d8', '#1e3c72']

fig12, ax12 = plt.subplots(figsize=(9, 5))
barres12 = ax12.barh(paiements, valeurs12,
                      color=couleurs12, height=0.5,
                      edgecolor='white', linewidth=1.5)
for barre, pct in zip(barres12, pourcentages12):
    ax12.text(
        barre.get_width() + 0.1,
        barre.get_y() + barre.get_height() / 2,
        pct, ha='left', va='center',
        fontweight='bold', fontsize=11, color='#1e3c72'
    )
ax12.set_title(
    'Figure 12 : Modèle de paiement préféré par les propriétaires (n=20)',
    fontsize=13, fontweight='bold', pad=15
)
ax12.set_xlabel('Nombre de propriétaires', fontsize=11)
ax12.set_xlim(0, 12)
ax12.grid(axis='x', alpha=0.3, linestyle='--')
ax12.spines['top'].set_visible(False)
ax12.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('figure12_modele_paiement.png', dpi=150, bbox_inches='tight')
plt.show()
print("Figure 12 sauvegardée ✅")


print("\n✅ TOUS LES 12 GRAPHIQUES GÉNÉRÉS !")
print("\nÉTUDIANTS :")
print("   figure1_situation_logement.png")
print("   figure2_ages.png")
print("   figure3_villes_etudiants.png")
print("   figure4_budgets.png")
print("   figure5_criteres.png")
print("   figure6_difficultes.png")
print("   figure7_interet_etudiants.png")
print("   figure8_fonctionnalites.png")
print("\nPROPRIÉTAIRES :")
print("   figure9_villes_proprietaires.png")
print("   figure10_methodes_publication.png")
print("   figure11_interet_proprietaires.png")
print("   figure12_modele_paiement.png")