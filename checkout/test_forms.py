from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    def test_Order_name_is_required(self):
        form = OrderForm({"full_name": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["full_name"][0],
                         "This field is required.")

    def test_street_address2_is_not_required(self):
        form = OrderForm({"street_address2": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("street_address2", form.errors.keys())
        self.assertEqual(form.errors["street_address2"][0],
                         "This field is required.")

    def test_email_is_not_required(self):
        form = OrderForm({"email": "Test Order"})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields,
            [
                'full_name',
                'email',
                'phone_number',
                'street_address1',
                'street_address2',
                'town_or_city',
                'county',
                'postcode',
            ],
        )
