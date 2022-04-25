from django.contrib import admin
from .models import Designer, Appointment


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ("designer",)
    search_fields = ["designer"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ("date", "designer")
    list_display = (
        "designer",
        "user_email",
        "first_name",
        "last_name",
        "age",
        "date",
        "time",
    )
    search_fields = ["date", "time"]
