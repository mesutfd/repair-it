# Generated by Django 4.0.6 on 2023-12-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_request', '0009_carrepairrequest_ergonomic'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrepairrequest',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Soft Delete'),
        ),
    ]
