from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    website_name = models.CharField(max_length=254, null=True, blank=True)
    category2 = models.CharField(max_length=254, null=True, blank=True)
    category_image = models.ImageField(null=True, blank=True)
    category_image_url = models.URLField(max_length=1024, null=True,
                                         blank=True)

    def __str__(self):
        return self.name

    def get_website_name(self):
        return self.website_name


class Product(models.Model):

    PROMO = [
        ("sale", "sale"),
        ("new_arrivals", "new_arrivals"),
    ]

    category = models.ForeignKey('Category', help_text="Please choose \
                                 an option from this list except for \
                                 'Sale' or 'New Arrivals'",
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL)
    category2 = models.CharField(max_length=254, help_text="Please choose \
                                 an option if this item is on sale or a \
                                 new arrival", null=True,
                                 blank=True, choices=PROMO)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currentprice = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    width = models.CharField(max_length=254, null=True, blank=True)
    height = models.CharField(max_length=254, null=True, blank=True)
    depth = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_sale_discount(self):
        """ Calculate cost with the discount """
        price = (self.price * (100 - 15) / 100)
        return price
