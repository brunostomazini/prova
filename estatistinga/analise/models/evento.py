from django.db import models
from .base_model import BaseModel
from ..enumerations import Esporte
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Evento(BaseModel):
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)]
    )

    local = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5)]
    )
    
    cidade = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(2)]
    )

    pais = models.CharField(
        max_length=80,
        validators=[MinLengthValidator(2)]
    )

    data = models.DateField()

    esporte = models.CharField(max_length=20, choices=Esporte)

    oficial = models.BooleanField(default=True)

    organizador = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        null=True,
        blank= True
    )

    capacidade = models.IntegerField(
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.esporte} - {self.cidade} - {self.pais} - {self.data.strftime("%d/%m/%Y")}"

    def clean(self):
        super().clean() #Lança as validações do da classe pai, garantindo as validações do pai
        today = timezone.localdate()
        if self.data <= today:
            raise ValidationError("A data marcada para o evento já passou, escolha outra data.")