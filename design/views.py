from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Appointment, Designer, User
from .forms import AppointmentForm, DesignerForm
from django_countries.fields import CountryField

# Create your views here.


def appointment_add(request):
    """ A view that shows a booking option """
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Successfully made appointment!')
            return redirect(reverse('appointment_show'))
        else:
            messages.error(request, 'Booking unsuccessful. Appointment did not go through!')
    else:
        form = AppointmentForm()

    template = 'design/appointment_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated appointment!')
            return redirect(reverse('appointment_show'))
        else:
            messages.error(request, 'Failed to update appointment. Please ensure all fields are valid!')
    else:
        form = AppointmentForm(instance=appointment)
        messages.info(request, f'You are amending appointment {appointment_id}')

    template = 'design/appointment_update.html'
    context = {
        'form': form,
        'appointment': appointment,
    }

    return render(request, template, context)


def appointment_show(request):
    """ A view that shows all bookings made by that user """
    appointments = request.user.hiuser.all()
    template = 'design/appointment_show.html'
    context = {
        "appointments": appointments,
        'on_page': True  # this will be applied to all contexts where we don't want to show what's in the shopping cart
    }

    return render(request, template, context)


def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.delete()
    messages.success(request, 'Appointment deleted successfully!')
    return redirect(reverse('appointment_show'))
