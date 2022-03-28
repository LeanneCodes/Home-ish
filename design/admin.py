from django.contrib import admin
from .models import Location, Appointment
from django_countries.fields import CountryField


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("store_locator", "designer")
    search_fields = ["store_locator", "designer"]


@admin.register(Appointment())
class AppointmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("location",)}
    list_filter = ("date", "location")
    list_display = (
        "location",
        "user_email",
        "first_name",
        "last_name",
        "age",
        "gender",
        "covid_safe",
        "date",
        "time",
    )
    search_fields = ["date", "time"]
