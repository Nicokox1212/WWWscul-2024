from django.shortcuts import render
from .models import Ryby, Okres_ochronny
# Create your views here.

def ryby_views(request):
    ryby = Ryby.objects.all()
    okres_ochronny = Okres_ochronny.objects.filter(wymiar_ochronny__gt=0)

    return render(request, 'ryby.html', {'ryby':ryby, 'okres_ochronny': okres_ochronny})


