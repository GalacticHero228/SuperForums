# Generated by Django 2.0.3 on 2018-04-07 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20180407_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='owner',
        ),
    ]