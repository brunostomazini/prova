from django.contrib import admin
from .models import Atleta, Estatistica, Evento

# Register your models here.
admin.site.register(Atleta)
admin.site.register(Estatistica)
admin.site.register(Evento)
