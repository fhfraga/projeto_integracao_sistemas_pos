# Generated by Django 5.0.4 on 2024-05-01 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAddress',
            new_name='Address',
        ),
    ]
