# Generated by Django 2.2.18 on 2021-03-21 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210321_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 13, 34, 57, 298391, tzinfo=utc)),
        ),
    ]
