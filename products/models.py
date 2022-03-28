from django.db import models
from django.conf import settings


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    website_name = models.CharField(max_length=254, null=True, blank=True)
    category2 = models.IntegerField(null=True, blank=True, default=0)
    category_image = models.ImageField(null=True, blank=True)
    category_image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_website_name(self):
        return self.website_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    category2 = models.IntegerField(null=True, blank=True, default=0)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    width = models.CharField(max_length=254, null=True, blank=True)
    height = models.CharField(max_length=254, null=True, blank=True)
    depth = models.CharField(max_length=254, null=True, blank=True)
    sale = models.IntegerField('85', blank=True, default=0)
    user_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wishlist')

    def __str__(self):
        return self.name


    def get_sale(self):
        """ Calculate cost with the discount """
        price = int(self.price * (100 - 15) / 100)
        return price
