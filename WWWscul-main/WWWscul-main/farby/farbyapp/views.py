from django.shortcuts import render
from .models import Farba
import math

def welcome(request):
    farby = Farba.objects.all()
    potrzebne_puszki = None
    powierzchnia = None

    if request.method == "POST":
        try:

            powierzchnia = float(request.POST.get("powierzchnia", 0))
            

            puszka_na_m2 = 4

   
            potrzebne_puszki = math.ceil(powierzchnia / puszka_na_m2)

        except ValueError:
            potrzebne_puszki = "Błąd danych"
    
    return render(request, 'farbyapp/index.html', {
        'farby': farby,
        'powierzchnia': powierzchnia,
        'potrzebne_puszki': potrzebne_puszki
    })
