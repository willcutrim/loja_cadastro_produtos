from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=40, null=False, blank=False)
    preco_do_produto = models.DecimalField(max_digits=5, blank=False, decimal_places=2)
    marca_do_produto = models.CharField(max_length=40, blank=False)
    
