from django.test import TestCase
from customer.models import *
from flight.models import *
from django.urls import reverse
# Create your tests here.



class CommentModelTest(TestCase):
    def setUp(self):
        user = Customer.objects.create(username="ss9",password="qw12re")
        Comment.objects.create(title="just a title",body="hi",customer=user)
    
    def test_textcontent(self):
        comment = Comment.objects.get(id=1)
        tit = f'{comment.title}'
        user_name = f'{comment.customer.username}'
        self.assertEqual(tit,"just a title")
        self.assertEqual(user_name,"ss9")



class OrderModelTest(TestCase):

    def setUp(self):
        way = Way.objects.create(origion='Tabriz',destination='Baku')
        airline = Airline.objects.create(name='ata airlines',phone='04143331111')
        airplane = Airplane.objects.create(name='Boeing',airline=airline,manufacturer='Airbus',year='2000-01-10')
        fly = Flight.objects.create(date='2028-12-04',time='00:00:00',price=20,remaining=21,airplane=airplane,way=way,seats=90)
        user = Customer.objects.create(username='test1',password='a123')
        tic = Ticket.objects.create(seat_number=24,unique_id=1,customer=user,fly=fly)
        order.objects.create(customer=user,ticket=tic)


    def test_order(self):
        Order = order.objects.get(id=1)
        org = f'{Order.ticket.fly.way.origion}'
        user = f'{Order.customer.username}'
        tic_status = f'{Order.ticket.status}'
        ord_status = f'{Order.status}'
        self.assertEqual(org,"Tabriz")
        self.assertEqual(user,"test1")
        self.assertEqual(tic_status,"check")
        self.assertEqual(ord_status,"check")









