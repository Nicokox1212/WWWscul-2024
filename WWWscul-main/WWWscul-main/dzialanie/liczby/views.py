from django.shortcuts import render
from .forms import Liczby

def dodaj(request):
    form = Liczby()
    context = {"form": form}

    if request.method == "POST":
        form = Liczby(request.POST)
        if form.is_valid():
            pole1 = form.cleaned_data['pole1']
            pole2 = form.cleaned_data['pole2']

            suma = pole1 + pole2
            roznica = pole1 - pole2
            iloczyn = pole1 * pole2
            try:
                iloraz = pole1 / pole2
            except ZeroDivisionError:
                iloraz = "Nie można dzielić przez 0"

            context.update({
                "suma": suma,
                "roznica": roznica,
                "iloczyn": iloczyn,
                "iloraz": iloraz,
            })

    return render(request, 'liczby/dodaj.html', context)
