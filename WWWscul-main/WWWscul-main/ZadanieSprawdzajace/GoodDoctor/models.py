from django.db import models

class Pacjent(models.Model):
    nazwisko = models.CharField(max_length=50)
    imie = models.CharField(max_length=50)
    miasto = models.CharField(max_length=50, default="Białystok")
    ulica = models.CharField(max_length=50)
    wiek = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.nazwisko} {self.imie}"
    

class Wizyta(models.Model):
    date = models.DateTimeField()
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    powod = models.TextField(null=True, blank=True)  
    uwagi = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.date} - {self.pacjent.imie} {self.pacjent.nazwisko}"