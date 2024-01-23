from django.test import TestCase
from flight.models import *


class FlightModelTest(TestCase):

    def setUp(self):
        date = '2020-12-04'
        time = '20:00:00'
        price = 30
        remining = 100
        seats = 120

        way = Way.objects.create(origion='Tabriz',destination='Baku')
        airline = Airline.objects.create(name='ata airlines',phone='04143331111')
        airplane = Airplane.objects.create(name='Boeing',airline=airline,manufacturer='Airbus',year='2000-01-10')
        Flight.objects.create(date=date,time=time,price=price,remaining=remining,airplane=airplane,way=way,seats=seats)


    def test_flight(self):
        flight = Flight.objects.get(id=1)
        time = f'{flight.time}'
        date = f'{flight.date}'
        org = f'{flight.way.origion}'
        dest = f'{flight.way.destination}'


        self.assertEqual(time,'20:00:00')
        self.assertEqual(date,'2020-12-04')
        self.assertEqual(org,'Tabriz')
        self.assertEqual(dest,'Baku')



