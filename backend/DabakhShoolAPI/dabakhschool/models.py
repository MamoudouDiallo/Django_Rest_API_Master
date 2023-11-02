from django.db import models

# Create your models here.
class Eleve(models.Model):
    nom = models.CharField(("nomEleve"), max_length=50)
    prenom = models.CharField(("prenomEleve"), max_length=50)
    age = models.IntegerField(("age"))
