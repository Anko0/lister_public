# Generated by Django 3.0 on 2020-03-25 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0007_auto_20200326_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(),
        ),
    ]
