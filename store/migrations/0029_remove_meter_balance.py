# Generated by Django 2.2.5 on 2020-04-25 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20200425_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meter',
            name='balance',
        ),
    ]
