from django.db import models
from django.utils.translation import gettext_lazy as _

class Esporte(models.TextChoices):
    FUTEBOL = "FUTEBOL"
    BASQUETE = "BASQUETE"
    CORRIDA = "CORRIDA"