# Generated by Django 2.2 on 2020-01-29 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200129_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 29, 11, 47, 40, 483504), verbose_name='Дата рождения'),
        ),
    ]
