# Generated by Django 3.2 on 2022-04-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_category2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_discount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
