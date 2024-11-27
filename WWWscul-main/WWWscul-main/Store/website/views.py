from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from website.models import Meeting
from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting , Room
from django.forms import modelform_factory
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
    rooms = Room.objects.all()
    return render(request, "website/rooms_list.html",{"rooms": rooms})

def new(request):
    if request.method=="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form=MeetingForm()
    return render(request, "website/new.html",{"form": form})
MeetingForm=modelform_factory(Meeting,exclude=[])