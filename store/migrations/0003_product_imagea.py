# Generated by Django 4.2.4 on 2024-04-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_shippingaddress_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageA',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
