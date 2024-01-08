from django.db import models
from django.contrib.auth.models import AbstractUser
from flight.models import Flight
from django.utils import timezone


class Customer(AbstractUser):

    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50,blank=True)



class Ticket(models.Model):
    seat_number = models.IntegerField()
    fly = models.ForeignKey(Flight,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=10,choices=[ ('check', 'Check Out'), ('paid', 'Paid')
                                                     ,('canceld', 'Canceld'),],default='check')
    unique_id =  models.CharField(max_length=100,default='',unique=True)

    def __str__(self):
        return  f" {self.unique_id}......{self.seat_number}"





class order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.PROTECT)
    status = models.CharField(max_length=10,choices=[ ('check', 'Check Out'), ('paid', 'Paid')
                                                     ,('canceld', 'Canceld'),],default='check')
    ticket = models.ForeignKey(to=Ticket,on_delete=models.PROTECT)
    date_time = models.DateTimeField(default=timezone.now)
    number = models.SmallIntegerField(default=1)


    def __str__(self):
        return  f"{self.customer } "

        

    def create(self,customer,tic):  
        o = order(customer=customer,ticket=tic)
        o.save()
        return True
        


class Operartor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,unique=True)
    email = models.EmailField(max_length=50)
    hour = models.SmallIntegerField()


    def __str__(self) -> str:
        return  f"{self.name } "



class Comment(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=20000)
    customer = models.ForeignKey(to=Customer,on_delete=models.PROTECT)
    operartor = models.ForeignKey(to=Operartor,on_delete=models.PROTECT,blank=True,null=True)
    reply = models.CharField(max_length=20000,null=True,blank=True)


    def __str__(self) -> str:
        return f"{self.title } "

