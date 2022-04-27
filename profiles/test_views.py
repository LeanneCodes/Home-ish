from django.test import TestCase
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404


class TestViews(TestCase):
    def test_get_profile(self):
        response = self.client.get("/profile")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_get_order_history(self):
        response = self.client.get("/checkout_success")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "checkout/checkout_success.html")

