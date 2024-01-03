from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.template import loader
from .models import Customer,order,Ticket
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from flight.models import Flight




class register(View):

    def get(self, request):
         form = UserForm()
         return render(request, "register.html", {"form":form})

    def post(self, request):
         form = UserForm(request.POST)
         if form.is_valid():
             form.cleaned_data["is_active"] = False
             form.save()
             return HttpResponse("Success!")
         else:
             return render(request, "register.html", {"form": form})



class Login(View):

    def get(self, request, *args, **kwargs):
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user:
            login(request, user)
            message = "Login successful!"
            if request.GET.get("next", None):
                return redirect(request.GET["next"])
        else:
            message = "User not found or wrong password!"

        template = loader.get_template('login.html')
        return HttpResponse(template.render({'message': message}, request))




class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "logout.html")
        else:
            return redirect("login")

    def post(self, request):
        logout(request)
        return HttpResponse("Logout successful!")


class Profile(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        user = Customer.objects.get( pk= request.user.id)
        template = loader.get_template('profile.html')
        return HttpResponse(template.render({'object':user}, request))

   

class OrderList(ListView):
    model = order
    template_name = "order_list.html"



class OrderDetail(DetailView):
    model = order
    template_name = "order_detail.html"
    


class Payment(LoginRequiredMixin,View):
     def get(self,request,*args, **kwargs):
        user = Customer.objects.get( pk= request.user.id)
        tic = order.objects.get(pk=kwargs['pk'])
        n = tic.number
        template = loader.get_template('payment.html')
        tic.status='paid'
        tic.save()
        flight = Flight.objects.get(id=tic.ticket.fly.id)
        flight.remaining -= n
        flight.save()

        return HttpResponse(template.render({'user':user,'ticket':tic}, request))



class Cancel(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        user = Customer.objects.get( pk= request.user.id)
        tic = order.objects.get(pk=kwargs['pk'])
        n = tic.number
        template = loader.get_template('payment.html')
        tic.status='canceld'
        tic.save()
        flight = Flight.objects.get(id=tic.ticket.fly.id)
        flight.remaining += n
        flight.save()
        return HttpResponse(template.render({'user':user,'ticket':tic}, request))



