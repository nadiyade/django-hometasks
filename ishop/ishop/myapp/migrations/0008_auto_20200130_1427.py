# Generated by Django 2.2 on 2020-01-30 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200130_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(1990, 1, 30, 2, 27, 57, 899066), verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='tovar',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
