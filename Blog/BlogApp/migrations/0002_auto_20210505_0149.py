# Generated by Django 3.2.1 on 2021-05-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.CharField(default='anonymous', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='post', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(default='anonymous', max_length=20),
        ),
    ]
