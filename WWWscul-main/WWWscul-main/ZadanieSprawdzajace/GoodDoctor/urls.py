from django.contrib import admin
from django.urls import path
from GoodDoctor.views import wizyty, details, pacjenci, dodaj_wizyte
from django.http import HttpResponseRedirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: HttpResponseRedirect("/wizyty/")),  
    path("details/<int:id>/", details, name="details"),
    path("pacjenci/", pacjenci, name="pacjenci"),
    path("wizyty/", wizyty, name="wizyty"),
    path("wizyty/nowa/", dodaj_wizyte, name="dodaj_wizyte"),
]
