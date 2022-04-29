from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True, verbose_name='Produto')
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')

    class Meta:
        db_table = 'produtos'

    def __str__(self):
        return self.nome
