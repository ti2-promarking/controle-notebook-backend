from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)

class Notebook(models.Model):
    disponivel = models.BooleanField(default=True)

class Aluguel(models.Model):
    data_aluguel = models.DateField()
    data_devolucao = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
