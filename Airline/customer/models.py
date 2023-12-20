from django.db import models
from django.contrib.auth.models import AbstractUser
from flight.models import Flight
from django.utils import timezone


class Customer(AbstractUser):

    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50,blank=True)
    password = models.CharField(max_length=30)




class Ticket(models.Model):
    seat_number = models.IntegerField()
    fly = models.ForeignKey(Flight,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)



class order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    status = models.CharField(max_length=10,choices=[ ('check', 'Check Out'), ('paid', 'Paid')
                                                     , ('canceld', 'Canceled')])
    ticket = models.ForeignKey(to=Ticket,on_delete=models.PROTECT)
    date_time = models.DateTimeField(default=timezone.now)
    number = models.SmallIntegerField(default=1)


