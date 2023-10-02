from django.db import models
from .gênero import Gênero

class Filme(models.Model):
    título = models.CharField(max_length=100)
    descrição = models.TextField()
    diretor = models.CharField(max_length=100)
    gênero = models.ForeignKey(Gênero, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.título