from django.db import models
from django.conf import settings

class Conversation(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='conversations_client'
    )

    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conversations_agent'
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    est_ouverte = models.BooleanField(default=True)

    def __str__(self):
        return f"Conversation {self.id} - {self.client.email}"

class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    expediteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_envoyes'
    )

    destinataire = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_recus'
    )

    contenu = models.TextField()
    est_lu = models.BooleanField(default=False)

    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id}"

class Notification(models.Model):
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    message = models.ForeignKey(
        'Message',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    TYPE_CHOICES = [
        ('MESSAGE', 'Message'),
        ('PAIEMENT', 'Paiement'),
        ('RESERVATION', 'Nouvelle réservation'),
        ('VALIDATION', 'Validation / Changement de statut'),
    ]

    type_notification = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='MESSAGE'
    )

    contenu = models.CharField(max_length=255)

    est_lu = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification ({self.type_notification}) pour {self.utilisateur.email}"
