# Generated by Django 2.2 on 2020-01-10 13:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200110_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='timeOfVisit',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 13, 42, 59, 421799, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='visit',
            name='visitedAnimal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Animal'),
        ),
        migrations.AddField(
            model_name='visit',
            name='whoVisited',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.Ticket'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='animalArrivalDate',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 13, 42, 59, 420801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketBought',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 13, 42, 59, 421799, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticketValid',
            field=models.DateField(default=datetime.datetime(2020, 1, 11, 13, 42, 59, 421799, tzinfo=utc)),
        ),
    ]
