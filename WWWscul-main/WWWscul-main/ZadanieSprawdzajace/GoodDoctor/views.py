from django.shortcuts import render, get_object_or_404
from GoodDoctor.models import Wizyta, Pacjent

# Widok listy wizyt
def wizyty(request):
    # Liczba wszystkich wizyt
    liczba_wizyt = Wizyta.objects.count()
    # Pobierz wszystkie wizyty
    wszystkie_wizyty = Wizyta.objects.all()
    return render(
        request,
        "GoodDoctor/wizyta.html",
        {
            "wizyty": liczba_wizyt,
            "all_wizyty": wszystkie_wizyty,
        },
    )

# Widok szczegółów pacjenta
def details(request, id):
    details = get_object_or_404(Pacjent, pk=id)
    return render(
        request,
        "GoodDoctor/detail.html",
        {
            "details": details,
        },
    )

# Widok listy pacjentów
def pacjenci(request):
    all_pacjenci = Pacjent.objects.all()
    return render(
        request,
        "GoodDoctor/pacjenci.html",
        {
            "all_pacjenci": all_pacjenci,
        },
    )


