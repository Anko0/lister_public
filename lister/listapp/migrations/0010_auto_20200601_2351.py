# Generated by Django 3.0 on 2020-06-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0009_auto_20200601_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code_token',
            field=models.CharField(default=None, max_length=34),
        ),
    ]
