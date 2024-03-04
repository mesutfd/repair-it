# Generated by Django 4.0.6 on 2023-12-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_request', '0008_alter_carrepairrequest_is_fixed'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrepairrequest',
            name='ergonomic',
            field=models.CharField(choices=[('Sedan', 'سدان'), ('SUV', 'شاسی بلند'), ('Pickup', 'آفرود')], default=None, max_length=200, verbose_name='ارگونومی'),
            preserve_default=False,
        ),
    ]
