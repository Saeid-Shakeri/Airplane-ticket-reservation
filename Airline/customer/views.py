from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from django.template import loader
from .models import Customer
from django.views import View

from django.contrib.auth import authenticate,login
from django.views.generic import ListView, DetailView




class register(View):

    def get(self, request):
         form = UserForm()
         return render(request, "register.html", {"form":form})

    def post(self, request):
         form = UserForm(request.POST)
         if form.is_valid():
             form.cleaned_data["is_active"] = False
             print( form.cleaned_data)
             form.save()
             print( form.cleaned_data["is_active"])
             return HttpResponse("Success!")
         else:
             return render(request, "register.html", {"form": form})



class Login(View):

    def get(self, request, *args, **kwargs):
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        print(request.POST["username"],request.POST["password"],user)
        if user:
         #   login(request, user)
            message = "Login successful!"
            if request.GET.get("next", None):
                return redirect(request.GET["next"])
        else:
            message = "User not found or wrong password!"

        template = loader.get_template('login.html')
        return HttpResponse(template.render({'message': message}, request))


 




#class Profile(DetailView):
    #model = Customer
    
  #  def get(self, request, *args, **kwargs):
   #     if request.user.is_authenticated:
    #       user_info = Customer.objects.filter()
     #      template = loader.get_template('profile.html')
      #     return HttpResponse(template.render({'user':user_info}, request))
       # else:
        #    return HttpResponse("You must be Login!")
