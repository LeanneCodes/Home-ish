from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    def test_UserProfile_category_is_required(self):
        form = UserProfileForm({"category": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["category"][0],
                         "This field is required.")

    def test_default_county_is_not_required(self):
        form = UserProfileForm({"default_county": "Test UserProfile"})
        self.assertFalse(form.is_valid())
