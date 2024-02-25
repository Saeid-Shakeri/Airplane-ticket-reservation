from django.test import TestCase, Client
from django.urls import reverse
from customer.models import *
from flight.models import *


class LoginViewTest(TestCase):
    def setUp(self):
        pass

        
    def test_view_url_exists_at_desired_location(self):

        response = self.client.get('/customer/login/')
        self.assertEqual(response.status_code,200)

    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        



class OrderListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        user = Customer.objects.create(username='test3',password='a1234')
        way = Way.objects.create(origion='Tabriz',destination='Baku')
        airline = Airline.objects.create(name='ata airlines',phone='04143331111')
        airplane = Airplane.objects.create(name='Boeing',airline=airline,manufacturer='Airbus',year='2000-01-10')
        fly = Flight.objects.create(date='2028-12-04',time='00:00:00',price=20,remaining=21,airplane=airplane,way=way,seats=90)
        tic = Ticket.objects.create(seat_number=24,unique_id=1,customer=user,fly=fly)
        order.objects.create(customer=user,ticket=tic)



    def test_view_url_exists_at_desired_location(self):

        self.client.login(username='test3',password='a1234')
        response = self.client.get('/customer/order/')
        self.assertEqual(response.status_code,302)

    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 302)

    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 302)
        


class OrderDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        user = Customer.objects.create(username='test3',password='a1234')
        way = Way.objects.create(origion='Tabriz',destination='Baku')
        airline = Airline.objects.create(name='ata airlines',phone='04143331111')
        airplane = Airplane.objects.create(name='Boeing',airline=airline,manufacturer='Airbus',year='2000-01-10')
        fly = Flight.objects.create(date='2028-12-04',time='00:00:00',price=20,remaining=21,airplane=airplane,way=way,seats=90)
        tic = Ticket.objects.create(seat_number=24,unique_id=1,customer=user,fly=fly)
        order.objects.create(customer=user,ticket=tic)



    def test_view_url_exists_at_desired_location(self):

        self.client.login(username='test3',password='a1234')
        response = self.client.get('/customer/order/1/')
        self.assertEqual(response.status_code,302)

    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('order_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('order_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        


