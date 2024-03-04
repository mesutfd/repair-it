from accounts.models import *
from django.db import models


class CarRepairRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    car_type = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name='نوع خودرو'
    )
    car_number = models.CharField(max_length=8, null=True, blank=True, verbose_name='پلاک خودرو')

    class CarErgonomic(models.TextChoices):
        sedan = 'Sedan', 'سدان'
        suv = 'SUV', 'شاسی بلند'
        pickup = 'Pickup', 'آفرود'

    ergonomic = models.CharField(max_length=200, choices=CarErgonomic.choices, verbose_name='ارگونومی')
    short_description = models.CharField(max_length=255, null=True, blank=True, verbose_name='عیب خودرو')
    description = models.TextField(null=True, blank=True, verbose_name='شرح خرابی')
    deliver_date = models.DateField(null=True, blank=True, auto_now=True, verbose_name='تاریخ تحویل خودرو به تعمیرگاه')
    costs_primary = models.IntegerField(null=True, blank=True, verbose_name='هزینه لوازم و قطعات')
    costs_secondary = models.IntegerField(null=True, blank=True, verbose_name='دستمزد')
    is_fixed = models.BooleanField(default=False, verbose_name='')
    is_deleted = models.BooleanField(default=False, verbose_name='Soft Delete')
