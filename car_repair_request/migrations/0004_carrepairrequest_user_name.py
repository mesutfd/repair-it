# Generated by Django 4.0.6 on 2022-07-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_request', '0003_remove_carrepairrequest_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrepairrequest',
            name='user_name',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='نام کاربری'),
        ),
    ]
