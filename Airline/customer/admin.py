from django.contrib import admin
from . models import *


admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(order)
admin.site.register(Comment)
admin.site.register(Operartor)
admin.site.register(EmailConfirmation)

