# Generated by Django 2.0 on 2018-02-01 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20180130_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grade',
            options={'ordering': ['order'], 'verbose_name': 'Grade'},
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to='crud.Class', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='school_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='crud.Class', verbose_name='Class'),
        ),
    ]
