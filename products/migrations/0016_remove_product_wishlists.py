# Generated by Django 3.2 on 2022-04-06 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_wishlists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='wishlists',
        ),
    ]