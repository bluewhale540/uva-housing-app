# Generated by Django 3.2.7 on 2021-11-07 22:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_review_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='type',
            new_name='is_house',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 22, 23, 49, 619498, tzinfo=utc), verbose_name='date posted'),
        ),
    ]
