from django.db import models

class Gênero(models.Model):
    descrição = models.CharField(max_length=100)
    def __str__(self):
        return self.descrição