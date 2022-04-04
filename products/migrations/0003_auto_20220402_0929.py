# Generated by Django 3.2 on 2022-04-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220402_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='category',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='subcategory',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]