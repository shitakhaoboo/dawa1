# Generated by Django 2.2.5 on 2019-12-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_daily_consumption_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_consumption',
            name='day',
            field=models.CharField(max_length=20),
        ),
    ]
