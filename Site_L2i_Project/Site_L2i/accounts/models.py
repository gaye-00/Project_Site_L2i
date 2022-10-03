from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
    is_etudiant = models.BooleanField(default=True)
    is_professeur = models.BooleanField(default=False)
