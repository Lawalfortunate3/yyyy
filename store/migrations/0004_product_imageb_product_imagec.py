# Generated by Django 4.2.4 on 2024-04-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_imagea'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imageB',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='imageC',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
