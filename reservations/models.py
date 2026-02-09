from django.db import models
from django.conf import settings
from prestations.models import FormuleTarifaire

class Reservation(models.Model):

    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée'),
        ('REJETEE', 'Rejetée'),
        ('TERMINEE', 'Terminée'),
    ]

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    formule = models.ForeignKey(
        FormuleTarifaire,
        on_delete=models.PROTECT,
        related_name='reservations'
    )

    date_evenement = models.DateField()
    heure_debut = models.TimeField()

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='EN_ATTENTE'
    )

    commentaire_client = models.TextField(blank=True)
    commentaire_admin = models.TextField(blank=True)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reservation #{self.id} - {self.client.email}"

class Paiement(models.Model):

    STATUT_PAIEMENT = [
        ('EN_ATTENTE', 'En attente'),
        ('PAYE', 'Payé'),
        ('ECHEC', 'Échec'),
    ]

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='paiements'
    )

    payeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='paiements'
    )

    montant = models.DecimalField(max_digits=10, decimal_places=2)

    mode_paiement = models.CharField(
        max_length=50,
        help_text="Mobile Money, Carte bancaire, Espèces, etc."
    )

    statut = models.CharField(
        max_length=20,
        choices=STATUT_PAIEMENT,
        default='EN_ATTENTE'
    )

    reference_transaction = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement {self.montant} - {self.statut}"
