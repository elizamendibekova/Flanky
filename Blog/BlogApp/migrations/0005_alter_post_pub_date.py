# Generated by Django 3.2.3 on 2021-05-23 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_auto_20210523_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 23, 7, 31, 33, 189639, tzinfo=utc)),
        ),
    ]
