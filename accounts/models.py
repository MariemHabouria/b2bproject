from django.db import models
from django.contrib.auth.models import AbstractUser
class Utilisateur(AbstractUser):
    is_poste = models.BooleanField(default=False)
    is_fournisseur = models.BooleanField(default=False)