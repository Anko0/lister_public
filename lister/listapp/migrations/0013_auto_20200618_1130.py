# Generated by Django 3.0 on 2020-06-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0012_code_code_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_executed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
