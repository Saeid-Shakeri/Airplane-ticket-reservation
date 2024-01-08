from django.db import models
from .Managers import *

class Way(models.Model):
    origion = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)


    def __str__(self) -> str:
        return  f"{self.origion }  To {self.destination}"



class Airline(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    logo = models.ImageField(null=True,blank=True,upload_to='logo/')


    
    def __str__(self) -> str:
        return  f"{self.name}"


class Airplane(models.Model):
    name = models.CharField(max_length=50)
    year = models.DateField(help_text='Year of construction')
    airline = models.ForeignKey(to=Airline,on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=30,help_text='Manufacturer')


    def __str__(self) -> str:
        return  f"{self.name}"


class Flight(models.Model):
    date = models.DateField()
    time = models.TimeField()
    price = models.PositiveSmallIntegerField()
    seats = models.IntegerField(help_text='The number of seats') 
    remaining = models.PositiveSmallIntegerField(help_text='Remaining tickets')
    cancel_percent = models.PositiveSmallIntegerField(help_text='Cancellation penalty percentage',default=0) #Cancellation penalty percentage
    way = models.ForeignKey(Way,on_delete= models.CASCADE)
    airplane = models.ForeignKey(Airplane,on_delete=models.CASCADE)

    objects = FlightManager()

    
    def __str__(self) -> str:
        return  f" {self.way} ........... {self.airplane }...........{self.date} "

