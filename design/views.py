from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment, Designer, User
from .forms import AppointmentForm, DesignerForm
from django_countries.fields import CountryField

# Create your views here.


def design(request):
    """ A view that shows a booking option """
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your appointment was created successfully!")
            return redirect("design_show")
        else:
            messages.warning(
                request,
                "Appointment was not successful. "
                "Check date or time chosen is not in the past. "
                "Please ensure all fields have valid inputs.",
            )
            return redirect("design")
    else:
        form = AppointmentForm
        context = {
            "form": form,
        }

    return render(request, 'design/design.html', context)


def design_show(request):
    """ A view that shows all bookings made by that user """
    items = request.user.hiuser.all()
    context = {"items": items}

    return render(request, 'design/design_show.html', context)


def design_update(request, item_id):
    """ A view that shows an option to update the booking """
    schedule = get_object_or_404(Appointment, id=item_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=schedule)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your appointment was updated successfully!")
            return redirect("design_show")
        else:
            messages.warning(
                request,
                "Appointment was not updated. "
                "Check date or time chosen is not in the past. "
                "Please ensure all fields have valid inputs.",
            )
    form = AppointmentForm
    context = {
        "form": form,
    }

    return render(request, 'design/design_update.html', context)


def design_delete(request, item_id):
    schedule = get_object_or_404(Appointment, id=item_id)
    if schedule.delete():
        messages.success(request, "Your appointment was deleted successfully!")
        return redirect("design_show")
    else:
        messages.warning(request, "Appointment was not deleted.")
