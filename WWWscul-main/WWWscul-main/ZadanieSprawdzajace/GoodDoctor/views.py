from django.shortcuts import render, get_object_or_404, redirect
from GoodDoctor.models import Wizyta, Pacjent
from .forms import WizytaForm


def wizyty(request):
    liczba_wizyt = Wizyta.objects.count()  
    wszystkie_wizyty = Wizyta.objects.all() 
    return render(
        request,
        "GoodDoctor/wizyta.html",
        {
            "wizyty": liczba_wizyt,
            "all_wizyty": wszystkie_wizyty,
        },
    )

def details(request, id):
    details = get_object_or_404(Pacjent, pk=id)
    return render(
        request,
        "GoodDoctor/detail.html",
        {
            "details": details,
        },
    )

def pacjenci(request):
    all_pacjenci = Pacjent.objects.all()
    return render(
        request,
        "GoodDoctor/pacjenci.html",
        {
            "all_pacjenci": all_pacjenci,
        },
    )




def dodaj_wizyte(request):
    from .models import Wizyta  # Import wewnątrz funkcji
    from .forms import WizytaForm
    if request.method == "POST":
        form = WizytaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wizyty")  # Przekierowanie na listę wizyt
    else:
        form = WizytaForm()

    return render(request, "GoodDoctor/new.html", {"form": form})

