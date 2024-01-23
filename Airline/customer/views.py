from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm,CommentForm,UserProfileForm
from django.template import loader
from .models import Customer,order,Comment,EmailConfirmation
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from flight.models import Flight
import logging
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
import uuid
from Airline.settings import isEmailConfirmation

from django.template.loader import render_to_string
from django.utils import timezone
from datetime import datetime, timedelta




logger = logging.getLogger(__name__)





def sendConfirmationEmail(req, form, user, renderHtml, sendAgain, againMessage):
    try:
        subject = 'Confirm your account'
        code = str(uuid.uuid4())
        expiration = timezone.make_aware(datetime.now() + timedelta(minutes=10))
        expiration_str = expiration.strftime(" %H:%M:%S")
        message = render_to_string('email_template.html', {"expiration_str": expiration_str,
                                                                      "username": user.username,
                                                                    
                                                                      "code": code})
        email_from = "admin@airline.com"
        recipient_list = [user.email]
        send_mail(subject=subject, message="", from_email=email_from, recipient_list=recipient_list, html_message=message)
        EmailConfirmation.objects.create(user=user, code=code, expires_on=expiration)
        logger.info(f"Email verification send successfully to {user.username}")
        if(sendAgain):
            return render(req, renderHtml, {"form": form, "status": "fail", "message": againMessage})
        return render(req, renderHtml, {"form": form, "status": "success", "message": "Sent a confirmation email"})
    except Exception as e:
        logger.error(str(e))
        return render(req, renderHtml, {"form": form, "status": "fail", "message": "Sending confirmation email failed: " + str(e)})


def confirmationView(req):
    code = req.GET.get("code", None)
    user = None
    try:
        if not code:
            raise Exception("No codes in url")
        confirmation = EmailConfirmation.objects.filter(code=code)
        user = confirmation[0].user
        user = Customer.objects.get(id=user.id)
        if not confirmation[0].is_valid():
            confirmation[0].delete()
            raise ExpiredException("Code has expired, sending another")
        user.is_active=True
        user.save()
        confirmation[0].delete()
        return render(req, "confirmation.html", {"status": "success","status_confirm":"success", "message": "You can now login"})
    except ExpiredException as e:
        logger.error(str(e))
        return sendConfirmationEmail(req, None, user, "confirmation.html", True, str(e))
    except Exception as e:
        logger.error(str(e))
        return render(req, "confirmation.html", {"status": "fail", "message": "Failed to confirm your email: " + str(e)})
    
class ExpiredException(Exception):
    pass


class register(View):

    def get(self, request):
         form = UserForm()
         return render(request, "register.html", {"form":form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.cleaned_data["is_active"] = False
            form.save()
            logger.info(f'user: {request.user} is registered.')
            userr = form.cleaned_data["username"]
            passwordd = form.cleaned_data["password1"]
            user = authenticate(username=userr,password=passwordd)
            if isEmailConfirmation:
                return sendConfirmationEmail(request, form, user, "register.html", False, None)
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
            logger.info(f'user: {request.user} is Logged in.')
           
              
            if request.GET.get("next", None):
                return redirect(request.GET["next"])
            return redirect('profile')

        else:
            message = "User not found or wrong password!"
            template = loader.get_template('login.html')
            return HttpResponse(template.render({'message': message}, request))





class Profile(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        user = Customer.objects.get( pk= request.user.id)
        template = loader.get_template('profile.html')
        return HttpResponse(template.render({'object':user}, request))

    def post(self, request):
        logger.info(f'user: {request.user.username} is logged out.')
        logout(request)
        return HttpResponse("Logout successful!")

   

class OrderList(LoginRequiredMixin,ListView):
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
        try:

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
            logger.info(f'user: {user} is Paid his ticket. order id:{ord.id} ')
            return HttpResponse(template.render({'user':user,'ticket':ord,'value':value}, request))

        except Exception as e:
            logger.error(str(e))
            return HttpResponse("Something Went Wrong!")




class Cancel(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        try:
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
            flight.save()
            logger.info(f'user: {user} is canceld his ticket. order id:{ord.id} ')
            return HttpResponse(template.render({'user':user,'ticket':ord,'value':value}, request))

        except Exception as e:
            logger.error(str(e))
            return HttpResponse("Something Went Wrong!")




    

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




def profile_update(request,pk):
    user = Customer.objects.get(id=request.user.id)
    if request.method == 'GET':
        userprofile_form = UserProfileForm(instance = user )
        return render(request, 'profile_update.html', {'userprofile_form': userprofile_form})

 
    if request.method == 'POST':
      form = UserProfileForm(request.POST,instance=user)
      if form.is_valid():
         form.save()     
         return redirect('profile')  
      return HttpResponse("Something went wrong")


def change_password(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('profile')
        else:
            HttpResponse('Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


























