from django.contrib import admin
from . models import Customer,Ticket,order


admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(order)