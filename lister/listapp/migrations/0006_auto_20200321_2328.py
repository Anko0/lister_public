# Generated by Django 3.0 on 2020-03-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0005_auto_20200321_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_isdone',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=5),
        ),
    ]