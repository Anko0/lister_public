# Generated by Django 3.0 on 2021-07-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0013_auto_20200618_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True),
        ),
    ]
