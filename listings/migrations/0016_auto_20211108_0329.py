# Generated by Django 3.2.7 on 2021-11-08 03:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_merge_0002_auto_20211101_1554_0014_auto_20211108_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date posted'),
        ),
    ]