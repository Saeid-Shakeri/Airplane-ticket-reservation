from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Flight, Airline
from .forms import SearchFrom
from django.template import loader
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class Index(View):

    def get(self, request):
    #  q =  Flight.objects.filter(date__gt=timezone.now())
      template = loader.get_template("index.html")
      return HttpResponse(template.render({}))



    def post(self, request):
    
         pass



class FlightList(ListView):

    model = Flight
    template_name = "flight_list.html"


class FlightDetail(DetailView):
    model = Flight
    template_name = "flight_detail.html"


class AirlineDetail(DetailView):
    model = Airline
    template_name = "airline_detail.html"



class Search(View):

    def get(self, request):
         form = SearchFrom()
         return render(request, "search.html", {"form":form})

  
    def post(self, request):
           try:       
                flight = Flight.objects.get(way = request.POST["way"],date=request.POST["date"])
                return render(request, "flight_detail.html", {"object":flight})

           except:
                return HttpResponse("this flight dosent exist!")








def airlines_view(request):

    q =  Airline.objects.all()
    template = loader.get_template("Airlines.html")
    return HttpResponse(template.render({'all_airlines': q}))




