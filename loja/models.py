from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    Categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=100,decimal_places=2)
    
    def __str__(self):
        return self.nome
