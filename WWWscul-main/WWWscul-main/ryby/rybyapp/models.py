from django.db import models

# Create your models here.

class Ryby(models.Model):
    nazwa = models.TextField()
    wystepowanie = models.TextField()
    styl_zycia = models.PositiveIntegerField()

    def __str__(self):
        return self.nazwa

class Okres_ochronny(models.Model):
    od_miesiaca = models.IntegerField()
    do_miesiaca = models.IntegerField()
    wymiar_ochronny = models.IntegerField()
    ryby_id = models.ForeignKey(Ryby, on_delete=models.CASCADE)

    def __str__(self):
        return f"Okres ochronny dla {self.ryby.nazwa}"