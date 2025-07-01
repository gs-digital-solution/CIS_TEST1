from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Etablissement(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    lycee_bilingue = models.BooleanField(default=False)  # Nouveau champ Oui/Non
    
    def __str__(self):
        return self.nom
    
class Eleve(models.Model):
    GENRE_CHOICES = [
        ('M', 'Masculine'),
        ('F', 'Féminin')
    ]
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)  # Champ NOM
    prenom = models.CharField(max_length=100)  # Champ PRENOM
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"  # Affichage combiné
    class Meta:
        verbose_name = "Élève"  # Nom singulier
        verbose_name_plural = "Élèves"  # Nom pluriel
