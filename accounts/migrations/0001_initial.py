# Generated by Django 4.0.6 on 2022-07-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='نام کاربری')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام خانوادگی')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/profile/', verbose_name='آواتار')),
                ('mobile', models.CharField(max_length=20, verbose_name='تلفن همراه')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
                ('car_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع خودرو')),
                ('car_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='پلاک خودرو')),
                ('short_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='عیب خودرو')),
                ('description', models.TextField(blank=True, null=True, verbose_name='شرح خرابی')),
                ('deliver_date', models.DateField(blank=True, null=True, verbose_name='تاریخ تحویل خودرو به تعمیرگاه')),
                ('costs_primary', models.IntegerField(blank=True, null=True, verbose_name='هزینه لوازم و قطعات')),
                ('costs_secondary', models.IntegerField(blank=True, null=True, verbose_name='دستمزد')),
                ('is_fixed', models.BooleanField(blank=True, default=False, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]