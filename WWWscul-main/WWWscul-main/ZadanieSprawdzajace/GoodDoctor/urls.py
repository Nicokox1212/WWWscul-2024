from django.contrib import admin
from django.urls import path
from GoodDoctor.views import wizyty, details, pacjenci

urlpatterns = [
    path("admin/", admin.site.urls),
    path("details/<int:id>/", details, name="details"),
    path("pacjenci/", pacjenci, name="pacjenci"),
    path("wizyty/", wizyty, name="wizyty"),
]
