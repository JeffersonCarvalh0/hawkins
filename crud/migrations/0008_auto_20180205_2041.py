# Generated by Django 2.0 on 2018-02-05 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20180205_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='student_body',
            new_name='students',
        ),
        migrations.RemoveField(
            model_name='student',
            name='current_class',
        ),
    ]