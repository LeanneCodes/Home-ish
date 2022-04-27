from django.test import TestCase
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404


class TestViews(TestCase):
    def test_get_checkout(self):
        response = self.client.get("/checkout")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout.html")

    def test_get_checkout_success(self):
        response = self.client.get("/checkout_success")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")
