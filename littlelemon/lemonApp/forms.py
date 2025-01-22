from django.forms import ModelForm
from .models import Booking
from django import forms


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'text',
                    'class': 'datepicker',
                    'placeholder': 'Select a date',
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'text',
                    'class': 'timepicker',
                    'placeholder': 'Select a time',
                }
            ),
        }
