from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from website.models import Meeting
from django.shortcuts import render, get_object_or_404
from .models import Meeting
# Create your views here.


def welcome(request):
    meetings = Meeting.objects.all()
    num_meetings = Meeting.objects.count()
    return render(request, "website/welcome.html",{"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def otobie(request):
    return HttpResponse("Ta strona jest o mnie, powiem krótko.")



def detail(request, id):
    meeting=Meeting.objects.get(pk=id)
    return render(request, "website/detail.html",{"meeting": meeting})

def rooms_list(request):
    room=Room.objects.all()
    return render(request, "website/rooms_list.html",{"rooms": room})