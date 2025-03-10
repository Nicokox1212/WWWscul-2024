from django.shortcuts import render, get_object_or_404
from .models import Ogloszenie, Uzytkownik

def index(request):
    ogloszenia = Ogloszenie.objects.select_related('uzytkownik').all()
    return render(request, 'index.html', {'ogloszenia': ogloszenia})


def tresc(request, ogloszenie_id):
    ogloszenie = get_object_or_404(Ogloszenie, id=ogloszenie_id)
    return render(request, 'tresc.html', {'ogloszenie': ogloszenie})


def uzytkownik(request):
    uzytkownicy = Uzytkownik.objects.all()
    return render(request, 'uzytkownik.html', {'uzytkownicy': uzytkownicy})


def ksiazka(request):
    ksiazki = Ogloszenie.objects.filter(kategoria=1)
    return render(request, 'ksiazka.html', {'ksiazki': ksiazki, 'ilosc': ksiazki.count()})