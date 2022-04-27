from django.test import TestCase
from .forms import AppointmentForm


class TestAppointmentForm(TestCase):
    def test_Appointment_name_is_required(self):
        form = AppointmentForm({"last_name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["last_name"][0],
                         "This field is required.")

    def test_street_address2_is_not_required(self):
        form = AppointmentForm({"street_address2": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("street_address2", form.errors.keys())
        self.assertEqual(form.errors["street_address2"][0],
                         "This field is required.")

    def test_time_is_not_required(self):
        form = AppointmentForm({"time": "Test Appointment"})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AppointmentForm()
        self.assertEqual(
            form.Meta.fields,
            [
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
            ],
        )
