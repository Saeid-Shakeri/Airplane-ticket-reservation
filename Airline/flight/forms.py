from django import forms
from .models import Flight
from customer.models import Ticket


class SearchFrom(forms.ModelForm):
    
    class Meta:
        model = Flight
        fields = ["way", "date"]


class TicketForm(forms.ModelForm):


    class Meta:
        model = Ticket
        fields = ["seat_number","unique_id"]
    
    
    #def __init__(self, *args, **kwargs):
     #   from django.forms.widgets import HiddenInput
      #  super(TicketForm, self).__init__(*args, **kwargs)
       # self.fields['unique_id'].widget = HiddenInput()


