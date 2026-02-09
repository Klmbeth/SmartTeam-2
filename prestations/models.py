from django.db import models

class Prestation(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='prestations/', blank=True, null=True)
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class FormuleTarifaire(models.Model):
    prestation = models.ForeignKey(
        Prestation,
        on_delete=models.CASCADE,
        related_name='formules'
    )
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} - {self.prestation.nom}"


