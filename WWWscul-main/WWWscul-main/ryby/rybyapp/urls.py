
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ryby_views, name='ryby_views'),
]
