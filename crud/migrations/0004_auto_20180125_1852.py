# Generated by Django 2.0 on 2018-01-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20180125_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registry',
            field=models.SlugField(max_length=30, unique=True, verbose_name='Registry'),
        ),
    ]
