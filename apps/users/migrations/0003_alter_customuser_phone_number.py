# Generated by Django 4.2.7 on 2023-11-29 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(regex='^996(\\d{3})\\d{2}\\d{2}\\d{2}$')], verbose_name='Телефон'),
        ),
    ]
