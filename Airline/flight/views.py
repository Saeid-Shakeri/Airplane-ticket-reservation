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
logger = logging.getLogger(__name__)






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
         message=''
         form = TicketForm()
         tic = Ticket.objects.filter(fly=pk).exclude(status="paid")
         return render(request, "ticket.html", {"form":form, "ticket_list":tic,'message': message})


    def post(self, request,*args, **kwargs):
            try:
                tic = Ticket.objects.get(unique_id=request.POST['unique_id'],seat_number=request.POST['seat_number'])
            except:
                return HttpResponse("You entered something wrong")

            if(order.create(self,customer=request.user,tic=tic)):
                message = "Added to your shopping cart"
                template = loader.get_template('ticket.html')
                return HttpResponse(template.render({'message': message}, request))

            else : return HttpResponse("Something went wrong")
           

           



class AirlineDetail(DetailView):
    model = Airline
    template_name = "airline_detail.html"



class Search(View):

    def get(self, request):
         form = SearchFrom()
         return render(request, "search.html", {"form":form})

    def post(self, request):       
        flight = Flight.objects.filter(way=request.POST["way"],date=request.POST["date"])
        if flight.exists():
            return render(request, "flight_list.html", {"flight_list":flight})

        else:
            return HttpResponse("This flight dosent exist!")


class CheapestFlights(View):

    def get(self, request):
        query = Flight.objects.cheapest()
        return render(request, "orderby_price.html", {"flight_list":query})











def airlines_view(request):

    q =  Airline.objects.all()
    template = loader.get_template("Airlines.html")
    return HttpResponse(template.render({'all_airlines': q}))




