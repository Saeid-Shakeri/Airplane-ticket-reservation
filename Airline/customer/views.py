from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm,CommentForm,EditProfile
from django.template import loader
from .models import Customer,order,Comment
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from flight.models import Flight
import logging
logger = logging.getLogger(__name__)





class register(View):

    def get(self, request):
         form = UserForm()
         return render(request, "register.html", {"form":form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.cleaned_data["is_active"] = False
            form.save()
            userr = form.cleaned_data["username"]
            passwordd = form.cleaned_data["password1"]
            user = authenticate(username=userr,password=passwordd)
            if user:
                login(request, user)
                template = loader.get_template('profile.html')
                return HttpResponse(template.render({'object':user}, request))    
        else:
            return render(request, "register.html", {"form": form})



class Login(View):

    def get(self, request, *args, **kwargs):
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
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

   
    def get(self,request):
        user = Customer.objects.get(pk=request.user.id) 
        q =  order.objects.filter(customer=user)
        if q.exists():
            template = loader.get_template("order_list.html")
            return HttpResponse(template.render({'object_list': q}))
        else : return HttpResponse("You haven't any order!")


class OrderDetail(LoginRequiredMixin,DetailView):
    model = order
    template_name = "order_detail.html"

    


class Payment(LoginRequiredMixin,View):
     def get(self,request,*args, **kwargs):
        user = Customer.objects.get(pk=request.user.id)
        ord = order.objects.get(pk=kwargs['pk'])
        tic = ord.ticket
        tic.status = 'paid'
        tic.save()
        n = ord.number
        template = loader.get_template('payment.html')
        ord.status='paid'
        ord.save()
        flight = Flight.objects.get(id=ord.ticket.fly.id)
        flight.remaining -= n
        flight.save()
        value= "-1"

        return HttpResponse(template.render({'user':user,'ticket':ord,'value':value}, request))



class Cancel(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        user = Customer.objects.get( pk= request.user.id)
        ord = order.objects.get(pk=kwargs['pk'])
        tic = ord.ticket
        tic.status = 'canceld'
        tic.save()
        n =ord.number
        template = loader.get_template('payment.html')
        ord.status='canceld'
        ord.save()
        flight = Flight.objects.get(id=ord.ticket.fly.id)
        flight.remaining += n
        value =  flight.price - ((flight.price * flight.cancel_percent)/100) 
        print(value)
        flight.save()
        logger.info(f'user: {user} is canceld his ticket. order id:{ord.id} ')
        return HttpResponse(template.render({'user':user,'ticket':ord,'value':value}, request))




    

class CommentList(ListView):
    model = Comment
    template_name = "comment_list.html"

   
    def get(self,request):
        user = Customer.objects.get(pk=request.user.id) 
        q =  Comment.objects.filter(customer=user)
        if q.exists():
            template = loader.get_template("comment_list.html")
            return HttpResponse(template.render({'object_list': q}))
        else : return HttpResponse("You haven't any Comment!")


class CommentDetail(DetailView):
    model = Comment
    template_name = "comment_detail.html"



class CommentView(LoginRequiredMixin,View):
    model = Comment
    template_name = "comment.html"

    def get(self, request):
        form = CommentForm()
        return render(request, "comment.html", {"form":form})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.customer = request.user
            new_comment.save()
            return HttpResponse("Your Comment has been Saved Successfully")    
        else:
            return HttpResponse("Something Went Wrong!")    




def profile_update(request, pk):
    user = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = EditProfile(request.POST)
        if form.is_valid():
            # update the existing `User` in the databases
            user.username = form.cleaned_data["username"]
            user.password = form.cleaned_data["password"]

            form.save()
            user.save()
            # redirect to the profile page of
            return redirect('profile')
    else:
        form = EditProfile()

    return render(request,
                'profile_update.html',
                {'form': form})
























