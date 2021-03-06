# Generated by Django 2.0 on 2018-02-23 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClassNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Number')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.SchoolClass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Student')),
            ],
            options={
                'verbose_name': 'Student class number',
                'ordering': ('number',),
            },
        ),
    ]
