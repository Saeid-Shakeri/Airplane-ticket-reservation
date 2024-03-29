from django.urls import path
from . import views





urlpatterns = [
       path('',views.Index.as_view(), name='index_view'),
       path('flight/',views.FlightList.as_view(),name="flight_list"),
       path("flight/<int:pk>/", views.FlightDetail.as_view(), name="flight_detail"),
       path('airlines/',views.airlines_view , name='airlines_view'),
       path('airline/<int:pk>/',views.AirlineDetail.as_view(),name="airline_detail"),
       path('search/',views.Search.as_view(),name="search"),
       path('<int:pk>/ticket/',views.Ticket_view.as_view(),name="ticket"),
       path('flight/orderby_price/',views.CheapestFlights.as_view(),name="order_by_price"),
       path('airplane/',views.AirplaneList.as_view(),name="airplane_list"),
       path('airplane/<int:pk>/',views.AirplaneDetail.as_view(),name="airplane_detail"),



 


     



]