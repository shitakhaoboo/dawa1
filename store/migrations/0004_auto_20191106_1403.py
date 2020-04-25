# Generated by Django 2.2.5 on 2019-11-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20191104_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='drugs',
            name='expiry',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
