# Generated by Django 3.2.7 on 2021-10-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20211029_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]
