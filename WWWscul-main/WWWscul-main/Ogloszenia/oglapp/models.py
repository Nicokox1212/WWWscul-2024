from django.db import models

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    telefon = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Ogloszenie(models.Model):
    kategoria = models.PositiveSmallIntegerField()
    podkategoria = models.PositiveSmallIntegerField()
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul