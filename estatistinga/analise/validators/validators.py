from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError



def age_validator(data):
    today = date.today()
    
    if data > today:
        raise ValidationError(
            "Data de nascimento invalida, tente novamente!"
        )

def event_date_validator(data):
    today = date.today()
    if data <= today:
        raise ValidationError(
            "O evento nao pode ser marcado para esta data"
            )
