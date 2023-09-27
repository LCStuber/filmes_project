from django.db import models

class Gênero(models.Model):
    descrição = models.CharField(max_length=100)
    def __str__(self):
        return self.descrição

# Create your models here.
class Filme(models.Model):
    título = models.CharField(max_length=100)
    descrição = models.TextField()
    diretor = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.título