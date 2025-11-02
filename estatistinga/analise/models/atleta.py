from django.db import models
from .base_model import BaseModel
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from ..enumerations import Esporte


class Atleta(BaseModel):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
        validators=[MinLengthValidator(5)]
    )
    cpf = models.CharField(
        verbose_name="Cpf",
        max_length=11,
        validators=[MinLengthValidator(11)], 
        unique=True
    )
    email = models.CharField(
        verbose_name="E-mail",
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    nascimento = models.DateField(verbose_name="Data de nascimento")
    altura = models.IntegerField(
        verbose_name="Altura", 
        validators=[MaxValueValidator(250)]
        )
    peso = models.DecimalField(
        verbose_name="Peso",
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(30), MaxValueValidator(250)]
        )
    esporte = models.CharField(verbose_name="Esporte", max_length=20, choices=Esporte)
    ativo = models.BooleanField(verbose_name="Ativo", default=True)

    def __str__(self):
        return f"{self.nome} - {self.esporte}"