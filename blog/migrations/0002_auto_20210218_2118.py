# Generated by Django 2.2.18 on 2021-02-18 18:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 18, 18, 18, 4, 949767, tzinfo=utc)),
        ),
    ]
