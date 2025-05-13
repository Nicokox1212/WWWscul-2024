from django.db import models


class Farba(models.Model):
    kolor = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)  # Deklaracja ceny jako Decimal
    pojemnosc = models.IntegerField()

    def __str__(self):
        return self.kolor

class Malowanie(models.Model):
    id_pomieszczenia = models.IntegerField()
    id_sciany = models.IntegerField()
    liczba_puszek = models.IntegerField()
    id_farby = models.ForeignKey(Farba, on_delete=models.CASCADE)
