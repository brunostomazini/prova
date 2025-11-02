from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator
from .atleta import Atleta
from .evento import Evento

class Estatistica(BaseModel):
    pontuacao = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    assistencias = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    faltas = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    cartoes= models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    minutos_jogados = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    distancia = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)
    
    atleta = models.ForeignKey(
        Atleta,
        on_delete=models.CASCADE,
        related_name='estatisticas'
    )
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        related_name='estatisticas'
    )

    def __str__(self):
        return f"{self.atleta.nome} - {self.evento.nome} - {self.atleta.esporte} - {self.pontuacao}"