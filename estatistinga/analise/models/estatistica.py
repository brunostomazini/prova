from django.db import models
from .base_model import BaseModel
from ..managers import EstatisticaManager
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .atleta import Atleta
from .evento import Evento
from django.utils import timezone
from datetime import date

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
        related_name="estatisticas"
    )

    def __str__(self):
        return f"{self.atleta.nome} - {self.evento.nome} - {self.atleta.esporte} - {self.pontuacao}"
    
    def clean(self):
        super().clean()
        if self.atleta.esporte != self.evento.esporte:
            raise ValidationError("O atleta não participa desse esporte!")
        
        today = date.today()
        idadeAtleta = self.atleta.nascimento
        idade = today.year - idadeAtleta.year - ((today.month, today.day) < (idadeAtleta.month, idadeAtleta.day))
        if idade < 12:
            raise ValidationError(
                "Idade minima para participação em eventos é de 12 anos."
                )
        
        if self.atleta.esporte == "CORRIDA":
            if not self.pontuacao or self.pontuacao < 1:
                raise ValidationError("Valor invalido, pontuação não pode ser menor que 1")
            if not self.distancia or self.distancia <1:
                raise ValidationError("Distancia minima é 1 ")
            if self.assistencias or self.faltas or self.cartoes or self.minutos_jogados:
                raise ValidationError("Assistencias, faltas, cartoes e minutos jogados devem ser valores nulos.")
        else:
            if not self.pontuacao or self.pontuacao < 0:
                raise ValidationError("Pontuação invalida")
            if self.assistencias < 0:
                raise ValidationError("Numero de assistencias invalido")
            if self.faltas < 0:
                raise ValidationError("Numero faltas invalido")
            if self.cartoes < 0:
                raise ValidationError("Numero de cartões invalido")
            self.distancia = None
    
    objects = EstatisticaManager()