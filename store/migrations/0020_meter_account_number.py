# Generated by Django 2.2.5 on 2019-12-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20191226_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='meter',
            name='account_number',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
