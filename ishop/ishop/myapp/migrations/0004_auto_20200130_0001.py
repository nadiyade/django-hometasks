# Generated by Django 2.2 on 2020-01-29 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200129_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 29, 12, 1, 56, 341400), verbose_name='Дата рождения'),
        ),
    ]
