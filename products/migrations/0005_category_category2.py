# Generated by Django 3.2 on 2022-03-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category2'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
