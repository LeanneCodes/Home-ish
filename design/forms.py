from django import forms
from django.forms import ModelForm
from .models import Appointment
from django_countries.fields import CountryField


# The fields available to iterate through in the user interface
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "first_name",
            "last_name",
            "user_email",
            "age",
            "gender",
            "user_phone",
            "covid_safe",
            "date",
            "time",
            "location",
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'user_email': 'Email Address',
            'age': 'Age',
            'gender': 'Gender',
            'user_phone': 'Phone Number',
            'covid_safe': 'Covid Safe',
            'date': 'Date',
            'time': 'Time',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postcode',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        self.fields['last_name'].widget.attrs['autofocus'] = Truev
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
