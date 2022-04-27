from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    def test_Product_category_is_required(self):
        form = ProductForm({"category": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["category"][0],
                         "This field is required.")

    def test_width_is_not_required(self):
        form = ProductForm({"width": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("width", form.errors.keys())
        self.assertEqual(form.errors["width"][0],
                         "This field is required.")

    def test_price_is_not_required(self):
        form = ProductForm({"price": "Test Product"})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(
            form.Meta.fields,
            [
                "category",
                "category2",
                "sku",
                "name",
                "description",
                "price",
                "currentprice",
                "rating",
                "image_url",
                "image",
                "width",
                "height",
                "depth",
            ],
        )
