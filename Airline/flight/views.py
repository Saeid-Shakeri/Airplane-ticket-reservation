from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Flight, Airline
from django.template import loader



def index_view(request):
    q =  Flight.objects.filter(date__gt=timezone.now())

    template = loader.get_template("index.html")
   
    return HttpResponse(template.render({'all_flights': q}))


def airlines_view(request):
    q =  Airline.objects.all()

    template = loader.get_template("Airlines.html")
   
    return HttpResponse(template.render({'all_airlines': q}))




