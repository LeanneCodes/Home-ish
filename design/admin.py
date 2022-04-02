from django.contrib import admin
from .models import Designer, Appointment
from django_countries.fields import CountryField


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ("designer",)
    search_fields = ["designer"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("designer",)}
    list_filter = ("date", "designer")
    list_display = (
        "designer",
        "user_email",
        "first_name",
        "last_name",
        "age",
        "gender",
        "date",
        "time",
    )
    search_fields = ["date", "time"]
