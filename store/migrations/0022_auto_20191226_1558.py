# Generated by Django 2.2.5 on 2019-12-26 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20191226_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='load_meter',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='load_meter',
            name='day',
            field=models.DateField(auto_now_add=True),
        ),
    ]
