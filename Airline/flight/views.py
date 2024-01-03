from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight, Airline
from .forms import SearchFrom,TicketForm
from django.template import loader
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from customer.models import order,Ticket
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import logging





class Index(View):

    def get(self, request):
      template = loader.get_template("index.html")
      return HttpResponse(template.render({}))


    def post(self, request):
         pass



class FlightList(ListView):

    model = Flight
    template_name = "flight_list.html"

    def get(self,request):
        q =  Flight.objects.filter(date__gt=timezone.now())

        template = loader.get_template("flight_list.html")
   
        return HttpResponse(template.render({'flight_list': q}))



class FlightDetail(DetailView):
    model = Flight
    template_name = "flight_detail.html"

    
    def post(self, request, *args, **kwargs):
        pass
        
        


class Ticket_view(LoginRequiredMixin,View):

    def get(self, request,pk):
         
         form = TicketForm()
         tic = Ticket.objects.filter(fly=pk).exclude(status="paid")
         return render(request, "ticket.html", {"form":form, "ticket_list":tic})


    def post(self, request,*args, **kwargs):
           tic = Ticket.objects.get(unique_id=request.POST['unique_id'])
           if(order.create(self,customer=request.user,tic=tic)):
               return HttpResponse("Added to your shopping cart")
        
           else : return HttpResponse("Something went wrong")
           

           



class AirlineDetail(DetailView):
    model = Airline
    template_name = "airline_detail.html"



class Search(View):

    def get(self, request):
         form = SearchFrom()
         return render(request, "search.html", {"form":form})

    def post(self, request):
           try:       
                flight = Flight.objects.filter(way=request.POST["way"],date=request.POST["date"])
                return render(request, "flight_list.html", {"flight_list":flight})

           except:
                return HttpResponse("this flight dosent exist!")













def airlines_view(request):

    q =  Airline.objects.all()
    template = loader.get_template("Airlines.html")
    return HttpResponse(template.render({'all_airlines': q}))




