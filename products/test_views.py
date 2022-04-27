from django.test import TestCase


class TestViews(TestCase):
    def test_get_all_products(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_get_add_product(self):
        response = self.client.get("/add_product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/add_product.html")

    def test_get_edit_product(self):
        response = self.client.get("/edit_product")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/edit_product.html")
