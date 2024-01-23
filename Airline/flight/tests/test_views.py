from django.test import TestCase
from flight.models import *
from django.urls import reverse


class FlightListViewTests(TestCase):
    def setUp(self):
       

        way = Way.objects.create(origion='Tabriz',destination='Baku')
        airline = Airline.objects.create(name='ata airlines',phone='04143331111')
        airplane = Airplane.objects.create(name='Boeing',airline=airline,manufacturer='Airbus',year='2000-01-10')
       
        Flight.objects.create(date='2020-12-04',time='00:00:00',price=30,remaining=100,airplane=airplane,way=way,seats=120)
        Flight.objects.create(date='2025-12-05',time='00:00:00',price=20,remaining=31,airplane=airplane,way=way,seats=70)
        Flight.objects.create(date='2025-12-06',time='00:00:00',price=200,remaining=1,airplane=airplane,way=way,seats=70)
        Flight.objects.create(date='2025-12-07',time='00:00:00',price=140,remaining=42,airplane=airplane,way=way,seats=70)
        Flight.objects.create(date='2025-12-08',time='00:00:00',price=200,remaining=30,airplane=airplane,way=way,seats=70)



    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/flight/')
        self.assertEqual(response.status_code, 200)

    
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('flight_list'))
        self.assertEqual(response.status_code, 200)

    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('flight_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight_list.html')
        

    def test_flights_count(self):
        response = self.client.get(reverse('flight_list'))
        self.assertEqual(len(response.context['flight_list']),4)





class FlightDetailViewTest(TestCase):

    def setUp(self):
        
        way = Way.objects.create(origion='Tabriz',destination='Kerman')
        airline = Airline.objects.create(name='mahan airlines',phone='04143331111',logo='km.jpg')
        airplane = Airplane.objects.create(name='Boeing 787',airline=airline,manufacturer='Airbus',year='2000-01-10')
       
        self.flight = Flight.objects.create(way=way,remaining=10,price=40,seats=80,
        date='2025-12-08',time='00:00:00',airplane=airplane)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/flight/1/')
        self.assertEqual(response.status_code, 200)
   
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('flight_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('flight_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight_detail.html')

    def test_view_has_book_in_context(self):
        response = self.client.get(reverse('flight_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('flight' in response.context)
        self.assertEqual(response.context['flight'], self.flight)

    def test_view_has_book_content(self):
        response = self.client.get(reverse('flight_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Tabriz')
