from django.test import TestCase


class TestViews(TestCase):
    def test_get_appointment_add(self):
        response = self.client.get("/appointment_add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "design/appointment_add.html")

    def test_get_appointment_update(self):
        response = self.client.get("/appointment_update")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "design/appointment_update.html")

    def test_get_appointment_show(self):
        response = self.client.get("/appointment_show")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "design/appointment_show.html")
