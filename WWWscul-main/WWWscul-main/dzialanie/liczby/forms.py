from django import forms

class Liczby(forms.Form):
    pole1 = forms.IntegerField(label="Liczba 1")
    pole2 = forms.IntegerField(label="Liczba 2")
