# Generated by Django 2.0 on 2018-01-05 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='partial_avg',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='total_avg',
        ),
    ]
