# Generated by Django 4.0.6 on 2022-07-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='car_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='car_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='costs_primary',
        ),
        migrations.RemoveField(
            model_name='user',
            name='costs_secondary',
        ),
        migrations.RemoveField(
            model_name='user',
            name='deliver_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_fixed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='short_description',
        ),
    ]
