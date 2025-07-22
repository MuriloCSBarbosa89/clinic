from django.db import models
from core.models_base import BaseModel

# Create your models here.
class Doctor(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nome")

    def __str__(self):
        return self.name

class Patient(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nome")
    birth_date = models.DateField(verbose_name="Data de Nascimento")

    def __str__(self):
        return self.name
