# Generated by Django 3.2 on 2022-04-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220402_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sub_category',
            name='category_image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='sub_category',
            name='website_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
