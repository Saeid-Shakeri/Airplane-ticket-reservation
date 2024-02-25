from django.contrib import admin
from .models import *
from django.http import HttpResponse
from django.urls import path
from django.template import loader
from django.utils import timezone
from django.shortcuts import render



admin.site.register(Way)
admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Airplane)



#Create a Target model
class list_of_flights(models.Model):
    class Meta:
        verbose_name_plural = 'list of flights'
        app_label = 'flight' # provide app name

# View
def target_view(request):
    q =  Flight.objects.all()

    template = loader.get_template("list_of_flights.html")
   
    return HttpResponse(template.render({'all_flights': q}))

# Register
class TargetAdmin(admin.ModelAdmin):
    model = list_of_flights

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name)
        #view_name = 'target_view'
        return [
            path('', target_view, name=view_name),
        ]

admin.site.register(list_of_flights, TargetAdmin)









#def my_custom_view(request):
    # perform some custom action
    # ...
 #   return render(request, 'my_custom_template.html')

# register the custom view
#admin.site.register_view('my-custom-view/', view=my_custom_view, name='My Custom View')

