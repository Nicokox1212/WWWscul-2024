from django.urls import path
from .views import index, tresc, uzytkownik, ksiazka

urlpatterns = [
    path('', index, name='index'),
    path('tresc/<int:ogloszenie_id>/', tresc, name='tresc'),
    path('uzytkownicy/', uzytkownik, name='uzytkownik'),
    path('ksiazki/', ksiazka, name='ksiazka'),
]
