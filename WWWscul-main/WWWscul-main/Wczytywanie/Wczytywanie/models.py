from django.db import models

class Osoba(models.Model):
    login = models.CharField(max_length=100, unique=True)
    haslo = models.CharField(max_length=255)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"