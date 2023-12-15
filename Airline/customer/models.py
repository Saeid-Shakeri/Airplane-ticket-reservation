from django.db import models
from django.contrib.auth.models import AbstractUser
from flight.models import Flight


class Customer(AbstractUser):

    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50,default="ex@2xample.com",blank=True)



class order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    status = models.CharField(max_length=10,choices=[ ('check', 'Check Out'), ('paid', 'Paid')
                                                     , ('canceld', 'Canceled')])
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE,default='0000')



class Ticket(models.Model):
    seat_number = models.IntegerField()
    fly = models.ForeignKey(Flight,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
