from django import forms
from .models import Appointment, Designer

# The fields available to iterate through in the user interface


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "first_name",
            "last_name",
            "user_email",
            "age",
            "user_phone",
            "date",
            "time",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "designer",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


widgets = {
        'date': forms.TextInput(attrs={'type': 'date'})

    }


class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = [
            "designer",
        ]

