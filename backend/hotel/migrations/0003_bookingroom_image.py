# Generated by Django 3.1 on 2020-08-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotelrooms_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingroom',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='booking/', verbose_name='Фото'),
        ),
    ]
