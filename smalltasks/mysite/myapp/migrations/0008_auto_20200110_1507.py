# Generated by Django 2.2 on 2020-01-10 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200110_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='animalArrivalDate',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 13, 7, 42, 276619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketBought',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 13, 7, 42, 276619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketValid',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 13, 7, 42, 276619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketVisitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Visitor'),
        ),
    ]