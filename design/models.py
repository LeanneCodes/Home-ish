import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Designer(models.Model):
    designer = models.CharField(primary_key=True, max_length=30)

    class Meta:
        ordering = ["designer"]

    def __str__(self):
        return self.designer


class Appointment(models.Model):
    TIMES = [
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
        ("20:00", "20:00"),
        ("21:00", "21:00"),
    ]

    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE,
        related_name="hiuser"
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False, null=False)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=11)
    date = models.DateField(
        max_length=10, validators=[MinValueValidator(datetime.date.today)]
    )
    time = models.CharField(help_text="Choose a time",
                            max_length=5, choices=TIMES)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    designer = models.ForeignKey("Designer", help_text="Choose a designer",
                                 null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.user_email
